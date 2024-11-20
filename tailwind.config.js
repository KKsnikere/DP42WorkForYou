/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: 'class',
  safelist: ['animate-[fade-in-down_1s_ease-in-out]'],
  theme: {
    extend: {
      colors:{
        colors: {
          primary: 'var(--primary-color)',         // Light Mode primary
          secondary: 'var(--secondary-color)',     // Light Mode secondary
          accent: 'var(--accent-color)',           // Light Mode accent
          red: '#D8ABAB',
          green: '#abced9',
          darker: '#97b6bf',
          greener: '#75967f',
  
          // Dark Mode Colors
          'primary-dark': 'var(--primary-dark)',   // Dark Mode primary
          'secondary-dark': 'var(--secondary-dark)', // Dark Mode secondary
          'accent-dark': 'var(--accent-dark)',     // Dark Mode accent
          'red-dark': '#9e7777',                   // Dark Mode red
          'green-dark': '#7e9c98',                 // Dark Mode green
          'darker-dark': '#6a8890',                // Dark Mode darker
          'greener-dark': '#4e5e56',               // Dark Mode greener

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
}
