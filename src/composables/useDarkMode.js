import { ref, onMounted } from 'vue';

export const useDarkMode = () => {
  const isDark = ref(false);

  const toggleDarkMode = () => {
    isDark.value = !isDark.value;
    document.documentElement.classList.toggle('dark', isDark.value);
    localStorage.setItem('theme', isDark.value ? 'dark' : 'light');
  };

  const initializeDarkMode = () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      isDark.value = true;
      document.documentElement.classList.add('dark');
    }
  };

  onMounted(() => {
    initializeDarkMode();
  });

  return { isDark, toggleDarkMode };
};
