const textEl    = document.getElementById('text');
const timeEl    = document.getElementById('time');
const dateEl    = document.getElementById('date');
const weatherEl = document.getElementById('weather');

// ===== Clock & Date =====
const DAYS   = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
const MONTHS = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];

function updateClock() {
  const now  = new Date();
  let   h    = now.getHours();
  const m    = String(now.getMinutes()).padStart(2, '0');
  const ampm = h >= 12 ? 'PM' : 'AM';
  h = h % 12 || 12;
  timeEl.textContent = `${String(h).padStart(2,'0')}:${m} ${ampm}`;

  const d   = String(now.getDate()).padStart(2,'0');
  const mo  = String(now.getMonth() + 1).padStart(2,'0');
  const y   = now.getFullYear();
  dateEl.textContent = `${d}/${mo}/${y}`;
}

setInterval(updateClock, 1000);
updateClock();

// ===== Weather =====
function fetchWeather() {
  fetch('/weather')
    .then(r => r.json())
    .then(d => { weatherEl.textContent = `${d.temp} °C`; })
    .catch(() => { weatherEl.textContent = '-- °C'; });
}

fetchWeather();
setInterval(fetchWeather, 10 * 60 * 1000);

// ===== Speech Stream =====
const es = new EventSource('/stream');

es.onmessage = (e) => {
  const data = JSON.parse(e.data);

  if (data.type === 'transcript') {
    textEl.classList.remove('flash');
    void textEl.offsetWidth;
    textEl.textContent = data.text;
    textEl.classList.add('flash');
  }
};
