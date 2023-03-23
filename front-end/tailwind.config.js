/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,ts}",],
  theme: {
    extend: {},
  },
    variants: {
    extend: {
      display: ['group - focus']
    },
  },
  plugins: [],
}
