# 3D Gun Viewer

An interactive, browser-based 3D viewer for gun models built with React, TypeScript, Vite, and the React Three Fiber ecosystem. Load the provided GLB model and explore it with orbit controls, switch lighting/environment presets, and interact with scene annotations.

The app uses:
- `@react-three/fiber` for rendering Three.js scenes with React
- `@react-three/drei` for helpers like `Environment` and `OrbitControls`
- `leva` for real-time UI controls (environment preset and blur)
- `valtio` for simple global state

## Demo / What It Does
- Renders a weapon model in a full-viewport canvas.
- Click the spherical markers in the scene to change viewpoints.
- Click specific weapon parts to change the depth-of-field target.
- Switch between environment lighting presets (sunset, dawn, night, warehouse, forest, apartment, studio, city, park, lobby).
- Tweak background blur via a Leva control.

Overlay hints are shown in the top-left corner of the app UI.

## Project Structure

Key files and folders:
- `index.html` — Vite entry HTML.
- `src/App.tsx` — App shell with `Canvas`, `Environment`, `OrbitControls`, Leva controls, and overlay.
- `src/components/Experience/` — Core 3D scene setup and interactions (models, annotations, effects).
- `src/components/Annotations/` — Annotation components and UI elements used in the scene.
- `src/store/` — Valtio store for global state (e.g., damping that toggles orbit behavior).
- `src/helpers/types.tsx` — Shared types, including environment preset typings.
- `public/collection2.glb` — Weapon 3D model.

## Getting Started

Prerequisites:
- Node.js 18+ and npm

Install dependencies:
```bash
npm install
```

Start the development server:
```bash
npm run dev
```

Build for production:
```bash
npm run build
```

Preview the production build locally:
```bash
npm run preview
```

## Usage and Controls
- Orbit camera: drag to rotate, scroll to zoom, pan as enabled by `OrbitControls`.
- When scene damping is enabled in the `valtio` store, orbit rotation/zoom are limited. Otherwise, full orbit is available.
- Use the Leva panel to:
  - Change `preset` (environment lighting).
  - Adjust `blur` (background blurriness via `Environment`).
- Click the spheres in the scene to jump to predefined viewpoints.
- Click weapon parts to refocus the depth of field target.

Tip: If the model doesn’t load, ensure `public/collection2.glb` exists and that your static file path is correct inside the scene components.

## Tech Stack
- React 18 + TypeScript
- Vite 7
- Three.js 0.168 via `@react-three/fiber`
- `@react-three/drei` helpers and `@react-three/postprocessing` (if used in scene)
- Leva (controls)
- Valtio (state)

## Scripts
Defined in `package.json`:
- `npm run dev` — Start Vite dev server with HMR.
- `npm run build` — Type-check and build for production.
- `npm run preview` — Preview the built app locally.
- `npm run lint` — Run ESLint.

## Development Notes
- Environments are provided by `drei`'s `<Environment preset={...} />` with presets typed via `Presets` in `src/helpers/types.tsx`.
- `src/App.tsx` shows how `OrbitControls` enable/disable behavior is tied to `store.damping` using `valtio`.
- The canvas camera is initialized at `position: [0, 0, 100]` and may be adjusted in code depending on your model scale.

## Roadmap / Ideas
- Add UI to toggle damping and other camera behaviors.
- Include more model files and a selector.
- Add mobile-friendly interaction tooltips.
- Export screenshots of the current view.

## Acknowledgements
- Built with the awesome React Three Fiber ecosystem: [react-three-fiber](https://github.com/pmndrs/react-three-fiber) and [drei](https://github.com/pmndrs/drei).
- Vite for fast dev builds.

## License
Specify a license for your project (e.g., MIT). If you add a `LICENSE` file, reference it here.

