// Self-authored review fixture, intended for Rust 2021 and panic=unwind.
// The current maintenance environment has not compiled or executed it.
use std::sync::Mutex;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub struct Balances {
    pub available: u64,
    pub reserved: u64,
}

struct RestoreOnFailure<'a> {
    state: &'a mut Balances,
    previous: Balances,
    committed: bool,
}

impl Drop for RestoreOnFailure<'_> {
    fn drop(&mut self) {
        if !self.committed {
            *self.state = self.previous;
        }
    }
}

// All observers use this same mutex. `prepare` must not reenter the mutex;
// it can return Err or panic, but has no irreversible external effect.
// A successful reservation preserves available + reserved.
pub fn reserve<F>(state: &Mutex<Balances>, amount: u64, prepare: F) -> Result<(), &'static str>
where
    F: FnOnce() -> Result<(), &'static str>,
{
    let mut guard = state.lock().map_err(|_| "poisoned")?;
    if amount > guard.available {
        return Err("insufficient");
    }
    let reserved = guard.reserved.checked_add(amount).ok_or("overflow")?;
    let previous = *guard;
    let mut rollback = RestoreOnFailure {
        state: &mut guard,
        previous,
        committed: false,
    };
    rollback.state.available -= amount;
    prepare()?;
    rollback.state.reserved = reserved;
    rollback.committed = true;
    Ok(())
}
