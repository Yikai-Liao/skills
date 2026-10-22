# Concurrency

<a id="concurrency"></a>

## Concurrency

<a id="poison"></a>

### Handling poison

Never reach inside a poisoned mutex to get at its insides, no matter how
tempting the use case may seem.
