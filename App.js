// CATEGORY_OPTIONS and ALL_EQUIPMENT moved outside App for global access
const ALL_EQUIPMENT = ['None', 'Dumbbell', 'Resistance Bands', 'Barbells', 'Kettlebells', 'Complete Gym'];
const CATEGORY_OPTIONS = [
  { tag: 'Strength', emoji: '💪' },
  { tag: 'Cardio', emoji: '🏃' },
  { tag: 'Endurance', emoji: '⏱️' },
  { tag: 'Wellness', emoji: '🧘' },
  { tag: 'Other', emoji: '🌟' }
];

// Muscle splits for each number of days
const MUSCLE_SPLITS = {
  1: ["Full Body"],
  2: ["Upper Body", "Lower Body"],
  3: ["Push", "Pull", "Legs"],
  4: ["Upper Body", "Lower Body", "Push", "Pull"],
  5: ["Push", "Pull", "Legs", "Upper Body", "Lower Body"],
  6: ["Push", "Pull", "Legs", "Push", "Pull", "Legs"],
  7: ["Push", "Pull", "Legs", "Upper Body", "Lower Body", "Full Body", "Active Recovery"]
};

// Example exercises for each split (for demo purposes)
const EXERCISES = {
  "Full Body": ["Squats", "Push-ups", "Rows", "Lunges", "Plank"],
  "Upper Body": ["Push-ups", "Rows", "Shoulder Press", "Bicep Curls", "Tricep Extensions"],
  "Lower Body": ["Squats", "Lunges", "Deadlifts", "Calf Raises", "Glute Bridge"],
  "Push": ["Push-ups", "Shoulder Press", "Tricep Dips", "Chest Press", "Incline Push-ups"],
  "Pull": ["Rows", "Pull-ups", "Bicep Curls", "Face Pulls", "Reverse Fly"],
  "Legs": ["Squats", "Lunges", "Deadlifts", "Calf Raises", "Glute Bridge"],
  "Active Recovery": ["Stretching", "Yoga", "Foam Rolling", "Walking"]
};

// Main React component for the Workout App (Front-End Only)

function App() {
  const [days, setDays] = React.useState(3);
  const [equipment, setEquipment] = React.useState(['None']);
  const [schedule, setSchedule] = React.useState([]);
  const [showSchedule, setShowSchedule] = React.useState(false);
  const [checkedIn, setCheckedIn] = React.useState([]);
  const [activeTab, setActiveTab] = React.useState('fitfolio');
  const [achievements, setAchievements] = React.useState([]);
  const [showAddAchievement, setShowAddAchievement] = React.useState(false);
  const [newAchievement, setNewAchievement] = React.useState({
    title: '',
    reflection: '',
    date: new Date().toISOString().slice(0, 10),
    category: '',
    emoji: '',
    photo: null,
    photoURL: '',
    mood: 3
  });
  const [dashboardMood, setDashboardMood] = React.useState([]);
  const [revealMilestone, setRevealMilestone] = React.useState(null);
  const [showLockScreen, setShowLockScreen] = React.useState(true);
  const [lockAchievement, setLockAchievement] = React.useState(null);
  const [clock, setClock] = React.useState(new Date());
  const [showRewind, setShowRewind] = React.useState(false);

  React.useEffect(() => {
    if (showLockScreen) {
      const interval = setInterval(() => setClock(new Date()), 1000);
      return () => clearInterval(interval);
    }
  }, [showLockScreen]);

  function handleEquipmentChange(e) {
    const value = e.target.value;
    setEquipment(prev => {
      if (value === 'None') return ['None'];
      const withoutNone = prev.filter(eq => eq !== 'None');
      return prev.includes(value)
        ? withoutNone.filter(eq => eq !== value)
        : [...withoutNone, value];
    });
  }

  // Generate workout plan in the frontend
  function generateWorkoutPlan(days, equipment) {
    const splits = MUSCLE_SPLITS[days] || MUSCLE_SPLITS[3];
    // Default parameters by split type
    const SPLIT_PARAMS = {
      'Push':     { sets: 4, reps: '8-12', rest: '60s' },
      'Pull':     { sets: 4, reps: '8-12', rest: '60s' },
      'Legs':     { sets: 4, reps: '10-15', rest: '75s' },
      'Upper Body': { sets: 3, reps: '10-15', rest: '60s' },
      'Lower Body': { sets: 3, reps: '12-15', rest: '75s' },
      'Full Body':  { sets: 3, reps: '10-15', rest: '60s' },
      'Active Recovery': { sets: 1, reps: 'Varies', rest: '-' }
    };
    return splits.map((split, idx) => {
      const exs = (EXERCISES[split] || EXERCISES["Full Body"]).slice(0, 5);
      const params = SPLIT_PARAMS[split] || { sets: 3, reps: '10-15', rest: '60s' };
      return {
        title: `Day ${idx + 1}: ${split}`,
        duration: '60-75 min',
        exercises: exs.map(name => ({
          name,
          sets: params.sets,
          reps: params.reps,
          rest: params.rest,
          desc: ''
        }))
      };
    });
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    if (equipment.length === 0) {
      alert("Please select at least one equipment option.");
      return;
    }
    setSchedule([]);
    setCheckedIn(Array(days).fill(false));
    setShowSchedule(true);
    // Generate plan in frontend
    setSchedule(generateWorkoutPlan(days, equipment));
  }

  function handleCheckIn(idx) {
    setCheckedIn(prev => prev.map((v, i) => (i === idx ? !v : v)));
  }

  function handleReset() {
    setActiveTab('planner');
    setShowSchedule(false);
    setSchedule([]);
    setEquipment(['None']);
    setDays(3);
    setCheckedIn([]);
    setGoal('');
    setShowGoalScreen(true);
  }

  function handleAddAchievement(e) {
    e.preventDefault();
    if (!newAchievement.title) return;
    const cat = CATEGORY_OPTIONS.find(c => c.tag === newAchievement.category) || CATEGORY_OPTIONS[4];
    const ach = {
      ...newAchievement,
      id: Date.now(),
      likes: 0,
      comments: [],
      emoji: cat.emoji,
      category: cat.tag
    };
    setRevealMilestone(ach);
    setTimeout(() => {
      setAchievements(prev => [ach, ...prev]);
      setDashboardMood(prev => [{ date: ach.date, mood: ach.mood }, ...prev]);
      setRevealMilestone(null);
    }, 3500);
    setNewAchievement({ title: '', reflection: '', date: new Date().toISOString().slice(0,10), category: '', emoji: '', photo: null, photoURL: '', mood: 3 });
    setShowAddAchievement(false);
  }

  function handlePhotoChange(e) {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = ev => setNewAchievement(a => ({ ...a, photo: file, photoURL: ev.target.result }));
      reader.readAsDataURL(file);
    }
  }

  function handleLike(id) {
    setAchievements(prev => prev.map(a => a.id === id ? { ...a, likes: a.likes + 1 } : a));
  }

  function handleComment(id, text) {
    setAchievements(prev => prev.map(a => a.id === id ? { ...a, comments: [...a.comments, text] } : a));
  }

  // Add handler to set lock screen achievement
  function handleSetLockAchievement(ach) {
    setLockAchievement(ach);
    setShowLockScreen(true);
  }

  // Animated Lock Screen
  if (showLockScreen) {
    // Use US Eastern Time for display
    const timeStr = clock.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'America/New_York' });
    const dateStr = clock.toLocaleDateString('en-US', { weekday: 'long', month: 'short', day: 'numeric', timeZone: 'America/New_York' });
    const bg = lockAchievement && lockAchievement.photoURL ? `url(${lockAchievement.photoURL})` : '#18181b';
    return (
      <div className="lock-screen" style={{
        position: 'fixed', inset: 0, zIndex: 1000, background: bg, backgroundSize: 'cover', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', transition: 'background 0.8s', animation: 'fadeIn 1.2s', color: '#f3f4f6', fontFamily: 'Poppins, Inter, Nunito, sans-serif'
      }}>
        <div style={{ textAlign: 'center', marginBottom: 32, animation: 'slideDown 1s' }}>
          <div style={{ fontSize: 54, fontWeight: 700, letterSpacing: 2, textShadow: '0 2px 12px #0008' }}>{timeStr} <span style={{fontSize:18, color:'#38b6ff'}}>EST</span></div>
          <div style={{ fontSize: 20, color: '#38b6ff', marginBottom: 12 }}>{dateStr}</div>
          <div style={{ fontSize: 22, fontWeight: 600, marginBottom: 8 }}>Welcome to your Fitfolio</div>
          {lockAchievement ? (
            <div style={{ margin: '18px 0', animation: 'fadeIn 1.2s 0.5s both' }}>
              <div style={{ fontSize: 32 }}>{lockAchievement.emoji}</div>
              <div style={{ fontWeight: 700, fontSize: 20 }}>{lockAchievement.title}</div>
              {lockAchievement.reflection && <div style={{ fontStyle: 'italic', color: '#a5b4fc', marginTop: 6 }}>{lockAchievement.reflection}</div>}
            </div>
          ) : (
            <div style={{ color: '#888', fontSize: 16, margin: '18px 0' }}>Set a favorite achievement as your lock screen!</div>
          )}
        </div>
        <button onClick={() => { setShowLockScreen(false); setActiveTab('planner'); }} style={{ background: '#38b6ff', color: '#fff', borderRadius: 18, padding: '14px 38px', fontWeight: 700, fontSize: 20, boxShadow: '0 2px 12px rgba(56,182,255,0.18)', border: 'none', cursor: 'pointer', transition: 'background 0.3s', animation: 'fadeIn 1.2s 0.8s both' }}>Proceed</button>
      </div>
    );
  }

  // --- Fitfolio Rewind logic ---
  // Top 3 milestones (by date)
  const top3 = achievements.slice(0, 3);
  // Sample keywords from reflections
  function getKeywords(reflection) {
    if (!reflection) return [];
    const stopwords = ['the','and','a','to','of','in','it','is','for','on','with','my','at','was','but','so','as','just','like','that','this','i','me','an','be','by','or','from','we','you','our','are','am','were','have','has','had','do','did','does','not','too','very','if','when','after','before','because','while','can','will','would','could','should','been','being','their','they','them','he','she','his','her','him','your','yours','mine','theirs','us','all','any','each','every','some','such','no','nor','only','own','same','than','then','there','these','those','through','up','down','out','off','over','under','again','further','once'];
    return reflection
      .toLowerCase()
      .replace(/[^a-z\s]/g, '')
      .split(/\s+/)
      .filter(w => w.length > 2 && !stopwords.includes(w));
  }
  // Top words frequency
  const allWords = achievements.flatMap(a => getKeywords(a.reflection));
  const wordFreq = allWords.reduce((acc, w) => { acc[w] = (acc[w]||0)+1; return acc; }, {});
  // --- Adjective filter for top words ---
  // List of common English adjectives (short, not exhaustive)
  const ADJECTIVES = [
    'amazing','awesome','bad','beautiful','better','brave','bright','brilliant','calm','challenging','clean','clear','cold','cool','crazy','creative','curious','dark','difficult','easy','energized','excited','fantastic','fast','fit','fresh','fun','good','great','happy','hard','healthy','hot','huge','important','incredible','intense','interesting','joyful','kind','long','loud','lucky','motivated','new','nice','old','peaceful','perfect','positive','powerful','proud','quick','quiet','relaxed','rough','sad','safe','scary','short','sick','simple','slow','small','strong','successful','tired','tough','warm','weak','weird','wild','wonderful','young','zesty','focused','determined','confident','relentless','unstoppable','steady','consistent','bold','fearless','grateful','optimistic','persistent','resilient','refreshed','rested','sore','sweaty','victorious','vibrant','fulfilled','accomplished','refreshed','rested','sore','sweaty','victorious','vibrant','fulfilled','accomplished','refreshed','rested','sore','sweaty','victorious','vibrant','fulfilled','accomplished'
  ];
  const topWords = Object.entries(wordFreq)
    .filter(([w]) => ADJECTIVES.includes(w))
    .sort((a,b) => b[1]-a[1])
    .slice(0,5)
    .map(([w])=>w);
  // Top win: highest mood
  const topWin = achievements.reduce((best, a) => (!best || a.mood > best.mood) ? a : best, null);
  // Reflection of the month: longest reflection
  const longestReflection = achievements.reduce((best, a) => (!best || (a.reflection||'').length > (best.reflection||'').length) ? a : best, null);
  // First time moment
  const firstTime = achievements.find(a => a.isFirstTime);
  // Photo highlight
  const photoHighlight = achievements.find(a => a.photoURL);

  return (
    <div className="workout-app" style={{ animation: 'fadeIn 1.2s' }}>
      <div className="brand-fitfolio">fitfolio</div>
      <nav style={{ display: 'flex', justifyContent: 'center', gap: 18, marginBottom: 18 }}>
        <button onClick={() => setActiveTab('planner')} className={activeTab === 'planner' ? 'active' : ''} aria-current={activeTab === 'planner' ? 'page' : undefined}>Planner</button>
        <button onClick={() => setActiveTab('fitfolio')} className={activeTab === 'fitfolio' ? 'active' : ''} aria-current={activeTab === 'fitfolio' ? 'page' : undefined}>Journal</button>
        <button onClick={() => setActiveTab('dashboard')} className={activeTab === 'dashboard' ? 'active' : ''} aria-current={activeTab === 'dashboard' ? 'page' : undefined}>Dashboard</button>
      </nav>

      {revealMilestone ? (
        <MilestoneRevealCard milestone={revealMilestone} />
      ) : activeTab === 'planner' ? (
        !showSchedule ? (
          <form className="setup-form" onSubmit={handleSubmit}>
            <h1>🏋️ Workout Split Planner</h1>
            <label>
              Days per week:
              <input
                type="number"
                min="1"
                max="7"
                value={days}
                onChange={e => setDays(Number(e.target.value))}
                required
              />
            </label>
            <fieldset>
              <legend>Select available equipment:</legend>
              <div className="equipment-options">
                {ALL_EQUIPMENT.map(eq => (
                  <label key={eq} className="equipment-label">
                    <input
                      type="checkbox"
                      value={eq}
                      checked={equipment.includes(eq)}
                      onChange={handleEquipmentChange}
                    />
                    {eq}
                  </label>
                ))}
              </div>
            </fieldset>
            <button type="submit">Generate Split Routine</button>
          </form>
        ) : (
          <div className="schedule-section">
            <h2>Your Weekly Split</h2>
            {schedule.length === 0 ? (
              <div style={{ color: '#888', margin: '16px 0' }}>Your personalized split will appear here after backend integration.</div>
            ) : (
              <ul className="schedule-list">
                {schedule.map((split, idx) => (
                  <li key={idx} className={checkedIn[idx] ? 'checked-in' : ''}>
                    <div>
                      <strong>{split.title}</strong>
                      <div><em>Approx. Duration:</em> {split.duration}</div>
                      <ul>
                        {split.exercises.map((ex, i) => (
                          <li key={`${ex.name}-${i}`}>
                            <b>{ex.name}</b> <br />
                            <span>Sets: {ex.sets} &nbsp; Reps: {ex.reps} &nbsp; Rest: {ex.rest}</span><br />
                            <span>{ex.desc}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                    <button onClick={() => handleCheckIn(idx)}>
                      {checkedIn[idx] ? '✅ Checked In' : 'Check In'}
                    </button>
                  </li>
                ))}
              </ul>
            )}
            <button onClick={handleReset} style={{ marginTop: '18px' }}>Start Over</button>
          </div>
        )
      ) : activeTab === 'fitfolio' ? (
        <div className="fitfolio-section" style={{ minHeight: 500, borderRadius: 18, padding: 0, animation: 'fadeInUp 0.8s' }}>
          <h1 style={{ textAlign: 'center', fontFamily: 'Poppins, Inter, Arial, sans-serif', fontWeight: 900, fontSize: '2rem', margin: '18px 0 12px 0', letterSpacing: 1 }}>Your Journal</h1>
          <div style={{ position: 'fixed', bottom: 32, right: 32, zIndex: 10 }}>
            <button className="add-milestone-btn" onClick={() => setShowAddAchievement(true)}>
              <span className="plus-icon"></span>
            </button>
          </div>
          {showAddAchievement && (
            <form className="achievement-form" onSubmit={handleAddAchievement}>
              <h2>What did you achieve today?</h2>
              <input type="text" placeholder="Milestone (e.g. Ran 5k)" value={newAchievement.title} onChange={e => setNewAchievement(a => ({ ...a, title: e.target.value }))} required />
              <select value={newAchievement.category} onChange={e => setNewAchievement(a => ({ ...a, category: e.target.value }))}>
                <option value="">Tag (optional)</option>
                {CATEGORY_OPTIONS.map(opt => <option key={opt.tag} value={opt.tag}>{opt.emoji} {opt.tag}</option>)}
              </select>
              <input type="date" value={newAchievement.date} onChange={e => setNewAchievement(a => ({ ...a, date: e.target.value }))} />
              <textarea placeholder="How did you feel? (Reflection)" value={newAchievement.reflection} onChange={e => setNewAchievement(a => ({ ...a, reflection: e.target.value }))} />
              <input type="file" accept="image/*" onChange={handlePhotoChange} />
              {newAchievement.photoURL && <img src={newAchievement.photoURL} alt="preview" style={{ maxWidth: 120, marginBottom: 10, borderRadius: 8 }} />}
              <label>Mood: <input type="range" min="1" max="5" value={newAchievement.mood} onChange={e => setNewAchievement(a => ({ ...a, mood: Number(e.target.value) }))} /></label>
              <label style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 10 }}>
                <input type="checkbox" checked={!!newAchievement.isFirstTime} onChange={e => setNewAchievement(a => ({ ...a, isFirstTime: e.target.checked }))} style={{ accentColor: '#38b6ff' }} />
                Is this your first time?
              </label>
              <button type="submit">Post</button>
              <button type="button" onClick={() => setShowAddAchievement(false)}>Cancel</button>
            </form>
          )}
          {/* Horizontally scrollable row for recent milestones */}
          {achievements.length > 0 && (
            <div className="fitfolio-carousel" style={{ display: 'flex', overflowX: 'auto', gap: 18, padding: '18px 0 12px 0', margin: '0 0 12px 0', scrollbarWidth: 'thin' }}>
              {achievements.slice(0, 5).map(a => (
                <div key={a.id} className="achievement-card" style={{ minWidth: 220, maxWidth: 260, flex: '0 0 auto', borderRadius: 16, padding: 16, boxShadow: '0 2px 12px rgba(0,0,0,0.18)', display: 'flex', flexDirection: 'column', gap: 8, animation: 'fadeInUp 0.7s', background: '#18181b', color: '#f3f4f6', border: '1.5px solid #23232a' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
                    <span style={{ color: '#a5b4fc', fontWeight: 700 }}>{a.category}</span>
                    <span style={{ marginLeft: 'auto', color: '#888', fontSize: '0.98em' }}>{a.date}</span>
                  </div>
                  <div style={{ fontWeight: 700, fontSize: '1.15em', fontFamily: 'Poppins, Inter, Arial, sans-serif' }}>{a.title}</div>
                  {a.photoURL && <img src={a.photoURL} alt="milestone" style={{ width: '100%', maxWidth: 180, borderRadius: 10, margin: '8px 0' }} />}
                  {a.reflection && <div style={{ fontStyle: 'italic', color: '#e5e7eb', background: '#23232a', borderRadius: 8, padding: 8 }}>{a.reflection}</div>}
                  <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginTop: 6 }}>
                    <button onClick={() => handleSetLockAchievement(a)} style={{ background: '#23232a', color: '#a5b4fc', borderRadius: 8, padding: '4px 10px', fontWeight: 600, fontSize: 13, marginLeft: 8, border: 'none', cursor: 'pointer', transition: 'background 0.2s' }}>Set as Lock</button>
                  </div>
                </div>
              ))}
            </div>
          )}
          {/* --- Fitfolio Highlight Summary --- */}
          {achievements.length >= 3 && (
            <div className="fitfolio-highlight">
              <h2 style={{ textAlign: 'center', color: '#38b6ff', fontFamily: 'Poppins', fontWeight: 900, margin: '18px 0 8px 0', letterSpacing: 1 }}>Your Journey So Far</h2>
              <div className="highlight-carousel" style={{ display: 'flex', overflowX: 'auto', gap: 18, padding: '8px 0 18px 0', margin: '0 0 18px 0', scrollbarWidth: 'thin' }}>
                {top3.map((a, i) => (
                  <div key={a.id} className="highlight-card" style={{ minWidth: 220, maxWidth: 260, flex: '0 0 auto', borderRadius: 16, padding: 16, boxShadow: '0 2px 12px rgba(56,182,255,0.13)', background: '#23232a', color: '#f3f4f6', border: '1.5px solid #23232a', display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                      <span style={{ fontSize: 32, marginRight: 2 }}>{(CATEGORY_OPTIONS.find(opt => opt.tag === a.category) || CATEGORY_OPTIONS[4]).emoji}</span>
                      <span style={{ color: '#a5b4fc', fontWeight: 700 }}>{a.date}</span>
                    </div>
                    <div style={{ fontWeight: 700, fontSize: '1.12em', fontFamily: 'Poppins' }}>{a.title}</div>
                    {a.reflection && (
                      <div style={{ fontSize: '0.98em', color: '#bbb', marginTop: 4, fontStyle: 'italic' }}>
                        {a.reflection}
                      </div>
                    )}
                  </div>
                ))}
              </div>
              <div style={{ textAlign: 'center', margin: '0 0 18px 0' }}>
                <button className="rewind-btn" onClick={() => setShowRewind(true)} style={{ background: '#38b6ff', color: '#fff', borderRadius: 8, padding: '10px 24px', fontWeight: 700, fontSize: '1.08em', border: 'none', fontFamily: 'Poppins', boxShadow: '0 2px 8px rgba(56,182,255,0.10)', transition: 'background 0.2s, color 0.2s' }}>Your Fitfolio Rewind</button>
              </div>
            </div>
          )}
          {/* --- Fitfolio Rewind Modal as Carousel --- */}
          {showRewind && (
            <div className="rewind-modal" style={{ position: 'fixed', top: 0, left: 0, width: '100vw', height: '100vh', background: 'rgba(24,24,27,0.96)', zIndex: 100, display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column' }}>
              <button onClick={() => setShowRewind(false)} style={{ position: 'absolute', top: 24, right: 32, background: 'none', color: '#bbb', border: 'none', fontSize: 32, cursor: 'pointer', zIndex: 2 }}>&times;</button>
              <h2 style={{ color: '#38b6ff', textAlign: 'center', fontFamily: 'Poppins', fontWeight: 900, marginBottom: 18, letterSpacing: 1, fontSize: '2rem', textShadow: '0 2px 12px #38b6ff22' }}>Your Fitfolio Rewind</h2>
              <div className="rewind-carousel">
                {/* Card 1: Top Win */}
                {topWin && (
                  <div className="rewind-card">
                    <div className="rewind-title">Top Win</div>
                    <div style={{ fontWeight: 700, fontSize: '1.1em' }}>{topWin.title}</div>
                    <div className="rewind-date">{topWin.date}</div>
                    <div className="rewind-reflection">{topWin.reflection}</div>
                  </div>
                )}
                {/* Card 2: Reflection of the Month */}
                {longestReflection && (
                  <div className="rewind-card">
                    <div className="rewind-title">Reflection of the Month</div>
                    <div style={{ fontWeight: 700, fontSize: '1.1em' }}>{longestReflection.title}</div>
                    <div className="rewind-date">{longestReflection.date}</div>
                    <div className="rewind-reflection">{longestReflection.reflection}</div>
                  </div>
                )}
                {/* Card 3: First Time Moment */}
                {firstTime && (
                  <div className="rewind-card">
                    <div className="rewind-title">First Time Moment</div>
                    <div style={{ fontWeight: 700, fontSize: '1.1em' }}>{firstTime.title}</div>
                    <div className="rewind-date">{firstTime.date}</div>
                    <div className="rewind-reflection">{firstTime.reflection}</div>
                  </div>
                )}
                {/* Card 4: Photo Highlight */}
                {photoHighlight && (
                  <div className="rewind-card">
                    <div className="rewind-title">Photo Highlight</div>
                    <div style={{ fontWeight: 700, fontSize: '1.1em' }}>{photoHighlight.title}</div>
                    <div className="rewind-date">{photoHighlight.date}</div>
                    <img className="rewind-img" src={photoHighlight.photoURL} alt="highlight" />
                    <div className="rewind-reflection">{photoHighlight.reflection}</div>
                  </div>
                )}
                {/* Card 5: Top Words */}
                {topWords.length > 0 && (
                  <div className="rewind-card top-words">
                    <div className="rewind-title">Top Words</div>
                    <div className="top-words-list">
                      {topWords.map(word => (
                        <span className="top-word" key={word}>{word}</span>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      ) : (
        <Dashboard achievements={achievements} moodData={dashboardMood} />
      )}

      <footer>
        <small>Front-end only: All split/exercise data will come from your Python backend. Edit this file to adjust UI only.</small>
      </footer>
    </div>
  );
}

// Other components unchanged
// Paste your existing MilestoneRevealCard, CommentBox, and Dashboard components here

function MilestoneRevealCard({ milestone }) {
  const [typedTitle, setTypedTitle] = React.useState('');
  React.useEffect(() => {
    let i = 0;
    const interval = setInterval(() => {
      setTypedTitle(milestone.title.slice(0, i + 1));
      i++;
      if (i >= milestone.title.length) clearInterval(interval);
    }, 60);
    return () => clearInterval(interval);
  }, [milestone.title]);
  return (
    <div className="reveal-overlay">
      <div className="confetti-bg"></div>
      <div className="reveal-card">
        <div className="reveal-emoji">{milestone.emoji}</div>
        <div className="reveal-date">{milestone.date}</div>
        <div className="reveal-title typewriter">{typedTitle}</div>
        {milestone.photoURL && <img src={milestone.photoURL} alt="milestone" className="reveal-photo" />}
        <div className="reveal-reflection pulse-glow">{milestone.reflection}</div>
      </div>
    </div>
  );
}

function CommentBox({ onComment, comments }) {
  const [text, setText] = React.useState('');
  return (
    <div style={{ background: '#f9fafb', borderRadius: 8, padding: 8 }}>
      <div style={{ marginBottom: 6, fontWeight: 600, color: '#2563eb' }}>Encouragement</div>
      <ul style={{ listStyle: 'none', padding: 0, margin: 0, marginBottom: 6 }}>
        {comments.map((c, i) => <li key={i} style={{ fontSize: '0.98em', marginBottom: 2 }}>💬 {c}</li>)}
      </ul>
      <form onSubmit={e => { e.preventDefault(); if (text) { onComment(text); setText(''); } }} style={{ display: 'flex', gap: 6 }}>
        <input value={text} onChange={e => setText(e.target.value)} placeholder="Write a comment..." style={{ flex: 1, borderRadius: 6, border: '1px solid #ddd', padding: 6 }} />
        <button type="submit" style={{ background: '#38b6ff', color: '#fff', borderRadius: 6, padding: '6px 12px', fontWeight: 600 }}>Post</button>
      </form>
    </div>
  );
}

function Dashboard({ achievements, moodData }) {
  const now = new Date();
  const thisMonth = now.toISOString().slice(0, 7);
  const milestonesThisMonth = achievements.filter(a => a.date.startsWith(thisMonth)).length;
  const catCounts = CATEGORY_OPTIONS.reduce((acc, c) => ({ ...acc, [c.tag]: achievements.filter(a => a.category === c.tag).length }), {});
  const moodPoints = moodData.slice().reverse().map((m, i) => ({ x: i, y: m.mood }));
  return (
    <div className="dashboard-section">
      <h1>Progress Dashboard</h1>
      <div className="dashboard-label">Milestones this month: <span className="dashboard-value">{milestonesThisMonth}</span></div>
      <div>
        <div className="dashboard-label">Categories:</div>
        <div className="dashboard-categories">
          {CATEGORY_OPTIONS.map(c => (
            <div key={c.tag} className="dashboard-category">
              {catCounts[c.tag] || 0}<br /><span style={{ fontSize: 15, opacity: 0.7 }}>{c.tag}</span>
            </div>
          ))}
        </div>
      </div>
      <div>
        <div className="dashboard-label">Mood Over Time:</div>
        <div className="dashboard-mood-bar">
          {moodPoints.length === 0 ? <span>No data yet</span> :
            moodPoints.map((p, i) => (
              <div key={i} className="dashboard-mood-point" style={{ height: `${p.y * 10 + 10}px` }} title={`Mood: ${p.y}`}></div>
            ))}
        </div>
        <div className="dashboard-mood-label">5 = Great, 1 = Tough</div>
      </div>
    </div>
  );
}

// Ensure this file has NO export or import statements and is pure JSX/JS for Babel in-browser.
// Add a fallback for React not loaded (for debugging in Live Server):
const rootElem = document.getElementById('root');
if (!rootElem) {
  document.body.innerHTML = '<div style="color:red;font-size:1.2em;padding:2em;text-align:center;">No <b>#root</b> element found. Make sure you are opening <b>Front end/index.html</b> in Live Server, not the project root or a folder.</div>';
} else if (typeof React === 'undefined' || typeof ReactDOM === 'undefined') {
  rootElem.innerHTML = '<div style="color:red;font-size:1.2em;padding:2em;text-align:center;">React or ReactDOM not loaded. Check your <b>index.html</b> script tags and reload.</div>';
} else {
  ReactDOM.createRoot(rootElem).render(<App />);
}

