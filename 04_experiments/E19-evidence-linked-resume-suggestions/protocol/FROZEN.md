# E19 Part A frozen inputs

Frozen at 2026-11-10T09:58:48Z (UTC), before any model call and before the harness code (ledger check, scorer, prompts, format check) was written.

These files must not change. A change means a new, labelled run folder. They are not committed to git because the owner has not asked for commits.

| File | sha256 |
|---|---|
| `protocol/thresholds.md` | `91ac71a9772bdc4109f73ceefe9f070c32c501ec908190693ef6c35a5ffffdc0` |
| `protocol/definitions.md` | `d766057e6de12ca495697e12ac7315fe7bed789337bfe0364383e9cbedce9450` |
| `data/gold/gold_sets.json` | `b342a24f8327776deeae3829d19425d488a8f53fa34ddeb2e6e0e13c1887f5ff` |
| `data/gold/format_gold.json` | `5f1d780a5a06545a5d14dcf3fc5404a89bf00c368d02df992e6a402ba8674c2e` |
| `data/postings.json` | `d101412e734b3ede2940c90f040ab01da0ddea6263d1531d65ea12f207ae551b` |
| `data/profile_A.json` | `0159d6bd7526ef32d7af92f7add66685c23d281fa834bcfd6559515092250676` |
| `data/profile_B.json` | `532ea4f08591557a21dfc49802b6c688ca003fe46340850d60ebe3be739cd43e` |
| `harness/make_format_fixtures.py` | `e918b0a2050817defd8a47c6440c4137cbf627dbd57af1aea8ed82a859dc7c74` |
| `data/format_fixtures\C01_docx_clean.docx` | `3a058153688c019d1b4b989cb83d3b2cfc05235798c478c62bd531003bf0e077` |
| `data/format_fixtures\C02_docx_clean_header_footer.docx` | `5d7c25e2754cfc4156abfaeff0c77703e42f6b79162e1b57366658b72a66b350` |
| `data/format_fixtures\C03_pdf_clean.pdf` | `321c13f48d178e0b85f14ae0327f8f2e804bbf31cd372e9be8f5f03ce8512c6c` |
| `data/format_fixtures\C04_pdf_clean_two_pages_link.pdf` | `ad626e9380f35bde0b98415ad82de34e9b9d8d3f3e36be05863126d523509448` |
| `data/format_fixtures\F01_docx_experience_as_image.docx` | `90164bf547f87879adf916cd5642fad0ad23f987263730c0e1219628fa9216c6` |
| `data/format_fixtures\F02_docx_experience_in_table.docx` | `5011f50d0f060292f5b78261fa804d470672a2e1a74dd194a18c132c384a1d27` |
| `data/format_fixtures\F03_docx_contact_in_header.docx` | `eac07e4670015e476cb31bc08abdb0e37296043044e00aa23d76eac334b4b632` |
| `data/format_fixtures\F04_docx_contact_in_footer.docx` | `5a766a1b9557d3791cef2d9d2ae9eefb5e22de0c2b23211e5cd5e13faaf0dfdb` |
| `data/format_fixtures\F05_docx_text_box.docx` | `ffbadc8ffcce504c4fb1bfc4a2cb5b9ec41c4348cb89c6d6ad6a5ad3dc526e66` |
| `data/format_fixtures\F06_docx_two_columns.docx` | `41f034b6c0e846844809a553de8a8b004da1235a3afe5843e92a24ecbb2a74d2` |
| `data/format_fixtures\F07_docx_no_headings.docx` | `b64f0ef512db9ac76d0676990ea97c0481faea8b7f1b964f0ff347c5cc5df88b` |
| `data/format_fixtures\F08_pdf_scanned_no_text_layer.pdf` | `b7bbfd853b261f6a59d921e078e4439c2586cf09132fd49931c1799bc7a2db32` |
| `data/format_fixtures\F09_pdf_contact_as_image.pdf` | `0a8d332f2f65cba636571cfcfc75e856e4126f3b2fa21618754f8a48b872388d` |
| `data/format_fixtures\F10_pdf_two_columns.pdf` | `4b33730f3d723f06017c47c612aeea4dbb619ef7fe18117165fa30ff4e6f8789` |
| `data/format_fixtures\F11_pdf_contact_in_header.pdf` | `fcf81b868012b772a2aa1c8a0f6098ac32e9c7916f3310d9d9113291a463503f` |
| `data/format_fixtures\F12_pdf_experience_in_table.pdf` | `304a2f48c9b2a985390ca1ce4f9df1e25e448741e89ab4475cea50b4188a63c2` |


## POST HOC format stress set (added 2026-11-10T10:05:37Z UTC)

Written after the frozen 16-file check had already run, and before the check was run on these files. Reported separately from the frozen result.

| File | sha256 |
|---|---|
| `data/gold/format_stress_gold.json` | `5f5051f98d1172ec47d5e073833a4514d0287ede9cb5e674e79ca866d3db3467` |
| `harness/make_format_stress.py` | `6c4633e9240f3ede7359de6292ee5804527547625c18ba3dcdc8d8f44f152e31` |
| `data/format_stress\S01_docx_clean_logo_in_header.docx` | `de880eb5a180e88f65cb02870ea74f75e1015b1387ca2fa1b446a3d15ace917a` |
| `data/format_stress\S02_docx_clean_caps_labels_no_styles.docx` | `86e86fec473670d70b585e27df32487496759fe6acf926938c5deaac893d947d` |
| `data/format_stress\S03_docx_three_columns.docx` | `065a816dd4e6b7d93c7e5cdad2b7af0b3d298d1a031d172a868c43dd2a5a9157` |
| `data/format_stress\S04_docx_layout_table.docx` | `b42375a823624977ce158d6c68842a27190f4197f569b3756441103672b0326c` |
| `data/format_stress\S05_docx_textbox_in_header.docx` | `1345d1fa71cad7a2fbab51dd56955fc818a3443e562328a1467cc94363edc6e3` |
| `data/format_stress\S06_pdf_three_columns.pdf` | `31ea0c57dbe55d88f843591cb101d16df7a7b3e131dd9900950d5072fd68ab7d` |
| `data/format_stress\S07_pdf_contact_in_footer.pdf` | `16ef48032b1f0d118a25aa023ea80deae80a62c77acb473211b5d8df7617694a` |
| `data/format_stress\S08_pdf_clean_logo.pdf` | `f2ba7fe0d373261a4ae54c61cf41f3c642eaea62043dec7541aa5617d43dcd99` |
| `data/format_stress\S09_pdf_clean_nonstandard_labels.pdf` | `09236333ef1ce44332288d7d5dd09147c04ef234dbc0cb17a50ec656c4a3e45c` |
| `data/format_stress\S10_docx_whole_page_picture.docx` | `438a60c28d2047220c241f185cbee870ae244b14e259451b4b4951e9cc0ad8b9` |
