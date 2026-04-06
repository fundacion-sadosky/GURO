🌐 [Castellano](CONTRIBUTING.md)

# Contribution guide

Contributions to the GURO project are welcome, regardless of your technical background: teachers, designers, developers and anyone interested can participate.

By contributing, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.en.md). Reading it is a prerequisite for any participation.

---

## Project scope — what is accepted and what is not

The GURO kit integrates proprietary components (adapter board, case, documentation) alongside third-party products (BBC Micro:bit, Kittenbot Robotbit, Robobloq Qoopers). This repository contains only the project's own components.

| Component | Modifiable in this repo? | License |
|---|---|---|
| GURO adapter board (KiCad) | Yes | GPLv3 |
| GURO case | Yes | GPLv3 |
| Documentation (`docs/`) | Yes | CC BY-SA 4.0 |
| Scripts (`scripts/`) | Yes | GPLv3 |
| Robobloq mechanical parts, motors, sensors | **No** | Property of Robobloq Co., Ltd. |
| BBC Micro:bit firmware / software | **No** | Micro:bit Educational Foundation licenses |
| Robotbit extension (MakeCode) | **No** | Kittenbot license |

### Accepted contributions:

- Improve the adapter board or the case (KiCad designs, maintainable 3D files such as openScad).
- Complete or correct the documentation (assembly guide, contribution guides, translations).
- Add or improve documentation generation scripts.
- Include original programming examples compatible with the project's licenses.
- Report bugs, ask questions or suggest improvements via issues.

### Not accepted:

- Contributions that modify, include or redistribute firmware, software or hardware designs of third-party products (Robobloq, Kittenbot, Micro:bit Educational Foundation, or others).
- Pre-compiled third-party binaries, including `.hex` files not produced by this project.
- Assets (images, text, code) with third-party copyright without verified compatibility with GPLv3 or CC BY-SA 4.0 as applicable.
- Personal data of any person, in particular of minors (see [Privacy and protection of minors](#privacy-and-protection-of-minors)).

If you want to modify third-party components (Micro:bit firmware, the Kittenbot extension, Qoopers parts), the right place is each manufacturer's repository, under their own licenses.

---

## How to contribute

### Teachers and writers

The documentation lives in the `docs/` folder, configured as an [Obsidian](https://obsidian.md) vault. You can edit it directly from the Obsidian application, without needing to use the terminal or know git.

See the [guide for writers](https://guro.readthedocs.io/contributing/for-writers/) for more details on the editing workflow and site conventions.

If you find a bug or want to suggest an improvement but do not want to edit directly, open an [issue](../../issues) describing the problem.

### Developers

See the [guide for developers](https://guro.readthedocs.io/contributing/for-developers/) for details on the environment, the tools used and the project conventions.

The standard workflow is:

1. Fork the repository.
2. Create a branch with a descriptive name (`fix/step-13-image`, `feat/english-translation`, etc.).
3. Make your changes and commit with clear messages.
4. Open a Pull Request to `main` describing what changes and why.

PRs must pass the repository's automated checks before being reviewed.

### Anyone

You can open an [issue](../../issues) to:

- Report a bug in the documentation or the designs.
- Suggest an improvement or new feature.
- Ask questions about the project.
- Share your experience using the kit in the classroom.

---

## License of contributions

By submitting a Pull Request to this repository, you declare that:

- Your contribution is your original work, or you have the right to submit it under the project's licenses.
- You publish your contribution under the repository's licenses: **GPLv3** for code and hardware designs, **CC BY-SA 4.0** for documentation.
- You understand that your contribution will be public and that others may use it under the terms of those licenses.

---

## Respect for third-party licenses

- Do not include code, firmware or assets from third parties without verifying license compatibility with GPLv3 or CC BY-SA 4.0, as applicable.
- If your contribution has an external dependency, document the dependency and its license; do not copy the component into the repository.
- The copyright of content created on Micro:bit Educational Foundation services belongs to whoever created it. If the creator is a minor, the copyright belongs to that minor. Keep this in mind when including programming examples.

---

## Privacy and protection of minors

The GURO kit is used in schools, so the project interacts directly with teachers and, through them, with students who may be minors.

- Do not include personally identifiable information (names, institutions, localities, recognizable photographs) in any repository file: code, documentation, examples, images or commit or issue comments.
- Do not include images or videos of minors without explicit authorization from their guardians.
- If you contribute examples created by your students, ensure they do not contain personal data and that you have the necessary authorizations according to the regulations applicable in your jurisdiction.
- All project spaces (issues, PRs, discussions, in-person events) must be safe spaces for every user, especially if they are minors.

For reference, see the [Safeguarding Policy of the Micro:bit Educational Foundation](https://microbit.org/safeguarding/).

---

## Credits

If your contribution is incorporated into the project, you may add your name to the credits table in `README.en.md`. The format is:

```
| Last name, First name | Role |
```

Roles can be combined: `Doc` (documentation), `SW` (software), `HW` (hardware), `Mechanics`, `Translation`, or other descriptive terms.

Open a PR that includes only the addition of your entry in the table.
