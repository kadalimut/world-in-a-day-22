// Sum up Sunday 22 November 2026 world news in one image.
// Node 22, standard library only, no network.
// The program copies the image beside it to the output folder.
// The image is drawn by tools/draw_image.py and stored as entry.png.
import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

// The output folder comes from MAKEFUN_OUTPUT_DIR outside the grader,
// or /output inside it. The copy is byte for byte: both grader runs
// must write the same bytes, and this program writes exactly the
// image file stored in the repository.
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
