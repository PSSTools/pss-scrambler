# pss-scrambler

PSS Scrambler obfuscates PSS source files by replacing user-specified identifiers with
randomly-selected English words. The structure of the code is preserved; only the names
change.

The usual reason to want this is sharing a reproducer. A parser bug or a tool crash is often
tied to the *shape* of a model rather than to what anything is called, and a scrambled copy
can be attached to an issue when the original cannot.

## Install

```sh
pip install pss-scrambler
```

## Use

```sh
pss-scrambler enc -o scrambled.pss model.pss [more.pss ...]
```

| Option | Effect |
|---|---|
| `-o`, `--output` | Output file. Defaults to `scrambled.pss`. |
| `-s`, `--seed` | Seed for choosing replacement words. The same seed gives the same renaming, so a scrambled reproducer can be regenerated. |
| `-c`, `--preserve-comments` | Keep comments from the input. Off by default — comments routinely carry the names the scrambling was meant to remove. |

PSS keywords, and identifiers defined by the PSS standard library, are left alone; renaming
those would produce something that is no longer PSS.

**Check the output before sending it anywhere.** This is a rename pass, not a security
control. String literals, file names, and anything embedded in a comment you chose to keep
are not obfuscated, and nothing here defends against someone correlating the structure of a
model with a known design.

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

Contributions are welcome — see
[the organization contributing guide](https://github.com/psstools/.github/blob/main/CONTRIBUTING.md).
Every commit needs a `Signed-off-by` trailer (`git commit -s`).
