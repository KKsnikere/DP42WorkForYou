/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: 'class', // Enables dark mode based on a class
  safelist: ['animate-[fade-in-down_1s_ease-in-out]'],
  theme: {
    extend: {
      colors: {
        // Light Theme Colors
        primary: '#dff1e7',
        secondary: '#f3f4f6',
        accent: '#aed8ab',
        red: '#D8ABAB',
        green: '#abced9',
        darker: '#97b6bf',
        greener: '#75967f',

        // Dark Theme Colors
        dark: {
          primary: '#121212', // Deep black for the main background
          secondary: '#1e293b', // Dark navy for cards or containers
          accent: '#6366f1', // Soft purple for highlighting elements
          red: '#ef4444', // Bright red for error or destructive actions
          green: '#22c55e', // Vibrant green for success indicators
          darker: '#0f172a', // Even darker shade for subtle depth
          greener: '#16a34a', // Rich green for interactive elements
        },        
      },
      boxShadow: {
        dark: '0 2px 3px rgba(0, 0, 0, 0.4)',
      },
    },
  },
  variants: {
    extend: {
      backgroundColor: ['dark'],
      textColor: ['dark'],
      borderColor: ['dark'], 
    },
  },
  plugins: [],
};
