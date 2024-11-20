import { ref, watchEffect } from 'vue';

export function useDarkMode() {
  // Check if dark mode is in localStorage
  const isDarkMode = ref(localStorage.getItem('darkMode') === 'true' || false);

  // Watch the state and apply dark mode class to <html> element
  watchEffect(() => {
    if (isDarkMode.value) {
      document.documentElement.classList.add('dark'); // Add dark class to root element
      localStorage.setItem('darkMode', 'true');        // Store preference in localStorage
    } else {
      document.documentElement.classList.remove('dark'); // Remove dark class from root element
      localStorage.setItem('darkMode', 'false');          // Store preference in localStorage
    }
  });

  // Toggle dark mode
  const toggleDarkMode = () => {
    isDarkMode.value = !isDarkMode.value;
  };

  return {
    isDarkMode,
    toggleDarkMode
  };
}
