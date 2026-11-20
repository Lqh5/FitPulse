/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#FFF3ED",
          100: "#FFE4D5",
          200: "#FFC7A8",
          300: "#FFA275",
          400: "#FF7D42",
          500: "#FF6B35", // Primary brand orange
          600: "#E55A2B",
          700: "#BF4622",
          800: "#99371D",
          900: "#7A2E19",
        },
      },
      fontFamily: {
        sans: [
          "-apple-system",
          "BlinkMacSystemFont",
          "Segoe UI",
          "Roboto",
          "Helvetica Neue",
          "Arial",
          "sans-serif",
        ],
      },
      maxWidth: {
        mobile: "390px",
      },
      height: {
        mobile: "844px",
      },
    },
  },
  plugins: [],
};