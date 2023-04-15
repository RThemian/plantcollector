/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  purge: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  content: [],
  theme: {
    extend: {},
  },
  plugins: [],
}