(function(){
  // theme.js - apply saved theme and wire up theme buttons
  const root = document.documentElement;
  const body = document.body;
  const storageKey = 'app2:theme';

  function applyTheme(name){
    body.classList.remove('theme-light','theme-dark','theme-accent');
    if(!name) name = 'theme-light';
    body.classList.add(name);
    // update active state on buttons
    document.querySelectorAll('.theme-controls button').forEach(btn=>{
      btn.classList.toggle('active', btn.dataset.theme === name);
    });
  }

  function init(){
    const saved = localStorage.getItem(storageKey) || 'theme-light';
    applyTheme(saved);

    document.addEventListener('click', e =>{
      const btn = e.target.closest && e.target.closest('.theme-controls button');
      if(!btn) return;
      const t = btn.dataset.theme;
      if(t){
        applyTheme(t);
        localStorage.setItem(storageKey, t);
      }
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
