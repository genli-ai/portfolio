import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Insights feed. Drop a new .md into src/content/research/ to add a report —
// frontmatter only. Each entry automatically gets a list row on the homepage
// and its own detail page at /insights/<filename>, which shows the bilingual
// abstract plus read / download links. reportUrl* = full HTML (read online),
// pdfUrl* = downloadable PDF (optional).
const research = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/research' }),
  schema: z.object({
    title: z.string(),
    titleZh: z.string(),
    type: z.enum(['flagship', 'note', 'drafting']),
    date: z.coerce.date(),
    summary: z.string(),
    summaryZh: z.string(),
    abstractEn: z.string().optional(),
    abstractZh: z.string().optional(),
    reportUrlEn: z.string().optional(),
    reportUrlZh: z.string().optional(),
    pdfUrlEn: z.string().optional(),
    pdfUrlZh: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { research };
