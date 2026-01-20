/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{js,jsx}", "./components/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#0d6efd",
        sidebar: "#212529",
        sidebarText: "#adb5bd",
      },
    },
  },
  plugins: [],
};
