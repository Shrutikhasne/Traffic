/**
 * Tailwind CSS Configuration
 */

module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#1A3C6D',
        'secondary': '#DC2626',
        'success': '#10B981',
        'warning': '#F59E0B',
      },
      fontFamily: {
        sans: ['system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
