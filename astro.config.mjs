// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

// For GitHub Pages deployment.
// If deploying to a project page (https://<user>.github.io/<repo>),
//   set both SITE and BASE env vars in the GH Actions workflow:
//     SITE=https://<user>.github.io BASE=/<repo>
// If deploying to a user/org page (https://<user>.github.io) or a custom domain,
//   leave BASE empty.

const site = process.env.SITE || 'https://reagan475614947.github.io';
const base = process.env.BASE || undefined;

// https://astro.build/config
export default defineConfig({
  site,
  base,
  vite: {
    plugins: [tailwindcss()]
  }
});
