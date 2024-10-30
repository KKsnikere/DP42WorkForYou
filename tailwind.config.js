/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  safelist: ['animate-[fade-in-down_1s_ease-in-out]'],
  theme: {
    extend: {
      colors:{
        primary: 'var(--primary-color)',
        secondary: 'var(--secondary-color)',
        accent: 'var(--accent-color)', 
        'red': '#D8ABAB',
        'green': '#abced9',
        'darker': '#97b6bf',
        'greener': '#75967f'

      },
      boxShadow: {
        'dark': '0 2px 3px rgba(0, 0, 0, 0.4)', // Customize the shadow color and spread
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

