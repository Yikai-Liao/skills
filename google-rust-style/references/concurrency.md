# Concurrency

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L957-L986); adapted under [CC BY 3.0](../LICENSE).

<a id="concurrency"></a>

## Concurrency

<a id="poison"></a>

### Handling poison

Never reach inside a poisoned mutex to get at its insides, no matter how
tempting the use case may seem.

<a id="async-await-chrome"></a>

### Don't use `async` / `.await` [chrome]

Don't use `async` / `.await` in Chromium.

<a id="std-thread"></a>

### Don't start new threads through the Rust standard library [chrome]

In Chromium, prefer to use sequences instead of threads.

<a id="fuchsia-mutex"></a>

### Use `fuchsia_sync::Mutex` [Fuchsia]

Use Fuchsia’s mutex type, rather than one from `std::sync` or `parking_lot`.
