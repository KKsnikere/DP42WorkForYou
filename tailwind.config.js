/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors:{
        primary: 'var(--primary-color)',
        secondary: 'var(--secondary-color)',
        accent: 'var(--accent-color)', 
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

