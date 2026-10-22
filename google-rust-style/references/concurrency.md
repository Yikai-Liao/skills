# Concurrency

Source: [Google Rust Style Guide](https://github.com/google/styleguide/blob/2ac1584cd3c9854760f02418ec24687ec1698fb8/rustguide.md#L957-L986); adapted under [CC BY 3.0](../LICENSE).

<a id="concurrency"></a>

## Concurrency

<a id="poison"></a>

### Handling poison

Never reach inside a poisoned mutex to get at its insides, no matter how
tempting the use case may seem.
