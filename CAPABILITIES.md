# Flux capability mapping

Compared with [MCPs at f0eed10abf31](https://github.com/AceDataCloud/MCPs/tree/f0eed10abf310824cb4c33d4944c63d3654ac95b/flux) and the public API contract at PlatformBackend `fa94598267a82545fb1afed6ee26bafd6cbb9ca7`.

The table maps service operations to Dify tools. Different MCP helper functions may use the same action selector or structured JSON input.

| MCP function | Dify equivalent | Notes |
|---|---|---|
| `flux_list_models` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `flux_list_actions` |  | Model/action selectors and the API reference; informational guidance does not submit a request. |
| `flux_get_task` | `flux_task_retrieve` | Set action=retrieve |
| `flux_get_tasks_batch` | `flux_tasks_retrieve_batch` | Set action=retrieve_batch |
| `flux_generate_image` | `flux_generate_image` | Set action=generate |
| `flux_edit_image` | `flux_edit_image` | Set action=edit |
| `flux_generate_video` | `flux_generate_video` |  |

## Parameter equivalents

- `flux_get_tasks_batch`: `task_ids` → ids.
- `flux_generate_video`: `request` → Expanded request fields (including nested JSON inputs).

## Verification boundary

Contract examples and regression tests cover request validation, transport and task handling. Actual Dify browser cases are recorded separately in `tests/e2e-results.json` and `tests/e2e-audit.json` when available. A schema test is not a successful paid generation. Unsupported service availability and untested advanced combinations must not be described as passed.
