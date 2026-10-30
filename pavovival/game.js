// PavoVival browser port.
// A line-by-line port of the libGDX game in core/src/main/java/com/g6/pavovival to
// JavaScript and Canvas 2D. Class names, numbers and rules follow the Java source;
// the world is the same 960x540 FitViewport with y pointing up, flipped only when drawing.
// Port additions (not in the original): a start screen (browsers need a click before
// audio), restart with R, Esc as a single-press pause, and touch controls.
"use strict";

const WORLD_W = 960, WORLD_H = 540;
const rand = (a, b) => a + Math.random() * (b - a);

// ---------------- entities ----------------
class Entity {
  constructor(tex, x, y, w, h) { this.tex = tex; this.x = x; this.y = y; this.w = w; this.h = h; this.vx = 0; this.vy = 0; this.alive = true; }
  bounds() { return { x: this.x, y: this.y, w: this.w, h: this.h }; }
  update(_dt) { throw new Error("abstract"); }
  render(g) { if (this.alive && this.tex) g.drawImage(this.tex, this.x, WORLD_H - this.y - this.h, this.w, this.h); }
}

class Enemy extends Entity {
  constructor(tex, x, y, w, h) { super(tex, x, y, w, h); this.hp = 1; }
  hit(damage) { this.hp -= damage; if (this.hp <= 0) this.alive = false; }
}

class Pavo extends Entity {
  constructor(tex, x, y) {
    super(tex, x, y, 144, 144);
    this.hp = 3; this.onGround = true; this.moveSpeed = 220; this.jumpVel = 450; this.gravity = -900;
    this.shootCooldown = 0.15; this.shootTimer = 0; this.facing = 1;
  }
  isDead() { return !this.alive || this.hp <= 0; }
  update(dt) {
    this.vy += this.gravity * dt; this.x += this.vx * dt; this.y += this.vy * dt;
    if (this.y <= 0) { this.y = 0; this.vy = 0; this.onGround = true; }
    if (this.shootTimer > 0) this.shootTimer -= dt;
  }
  moveLeft() { this.vx = -this.moveSpeed; this.facing = -1; }
  moveRight() { this.vx = this.moveSpeed; this.facing = 1; }
  stopX() { this.vx = 0; }
  jump() { if (this.onGround) { this.vy = this.jumpVel; this.onGround = false; } }
  canShoot() { return this.shootTimer <= 0; }
  didShoot() { this.shootTimer = this.shootCooldown; }
}

class Minion extends Enemy {
  constructor(tex, x, y) { super(tex, x, y, 110, 110); this.hp = 1; this.speed = 75; this.gravity = -900; }
  update(dt) { this.vy += this.gravity * dt; this.y += this.vy * dt; if (this.y <= 0) { this.y = 0; this.vy = 0; } this.x += this.vx * dt; }
  steerToward(p) { this.vx = p.x > this.x ? this.speed : -this.speed; }
}

class Bird extends Enemy {
  constructor(tex, x, y) {
    super(tex, x, y, tex.width, tex.height);
    this.hp = 3; this.vx = -110; this.t = 0; this.baseY = y;
    const TARGET_HEIGHT = 60;
    this.h = TARGET_HEIGHT; this.w = TARGET_HEIGHT * (tex.width / tex.height);
  }
  update(dt) {
    this.t += dt; this.x += this.vx * dt; this.y = this.baseY + 20 * Math.sin(6 * this.t);
    if (this.x + this.w < -16) this.alive = false;
  }
}

class Bullet extends Entity {
  constructor(tex, x, y, facing, fromEnemy) { super(tex, x, y, 20, 12); this.speed = 520; this.dmg = 1; this.fromEnemy = fromEnemy; this.vx = this.speed * facing; }
  static playerBullet(tex, x, y, facing) { return new Bullet(tex, x, y, facing, false); }
  static enemyBullet(tex, x, y, facing) { return new Bullet(tex, x, y, facing, true); }
  update(dt) { this.x += this.vx * dt; if (this.x < -100 || this.x > 2000) this.alive = false; }
  damage() { return this.dmg; }
}

class Boss extends Enemy {
  constructor(tex, x, y) {
    super(tex, x, y, 248, 248); this.hp = 5;
    this.speed = 60; this.gravity = -900; this.jumpVel = 400; this.jumpTimer = 0; this.shootTimer = 0; this.shootInterval = 1.1;
  }
  update(dt) {
    this.vy += this.gravity * dt; this.y += this.vy * dt; if (this.y <= 0) { this.y = 0; this.vy = 0; }
    this.x += this.vx * dt;
    if (this.jumpTimer > 0) this.jumpTimer -= dt;
    if (this.shootTimer > 0) this.shootTimer -= dt;
  }
  pursue(p) {
    this.vx = p.x > this.x ? this.speed : -this.speed;
    if (this.jumpTimer <= 0 && Math.random() < 0.004 && this.y === 0) { this.vy = this.jumpVel; this.jumpTimer = 1.5; }
  }
  maybeShoot(enemyBullets, bossBulletTex, target) {
    if (this.shootTimer > 0) return;
    const dir = target.x < this.x ? -1 : 1;
    enemyBullets.push(Bullet.enemyBullet(bossBulletTex, this.x + (dir === 1 ? this.w : -8), this.y + this.h * 0.55, dir));
    this.shootTimer = this.shootInterval;
  }
}

// ---------------- controllers ----------------
class LevelController {
  constructor() { this.level = 1; this.spawnedInWave = 0; this.killedInWave = 0; this.totalKills = 0; this.bossSpawned = false; }
  waveSize() { return this.level === 2 ? 10 : this.level === 3 ? 15 : 5; }
  onMinionSpawned() { this.spawnedInWave++; }
  onMinionKilled() { this.killedInWave++; this.totalKills++; }
  canSpawnMoreThisWave() { return this.spawnedInWave < this.waveSize(); }
  isWaveCleared() { return this.killedInWave >= this.waveSize(); }
  advanceLevelIfCleared() { if (this.isWaveCleared() && this.level < 3) { this.level++; this.resetWave(); } }
  shouldSpawnBoss() { return this.level === 3 && this.isWaveCleared() && !this.bossSpawned; }
  resetWave() { this.spawnedInWave = 0; this.killedInWave = 0; }
}

class Spawn {
  constructor(assets, levels) { this.assets = assets; this.levels = levels; this.spawnTimer = 0; this.spawnInterval = 1.1; }
  maxActiveForLevel(level) { return level === 2 ? 4 : level === 3 ? 5 : 3; }
  update(dt, enemies, pavo) {
    if (this.levels.shouldSpawnBoss()) return;
    let active = 0;
    for (const e of enemies) if (e.alive && (e instanceof Minion || e instanceof Bird)) active++;
    this.spawnTimer -= dt;
    const canSpawn = this.levels.canSpawnMoreThisWave() && active < this.maxActiveForLevel(this.levels.level) && this.spawnTimer <= 0;
    if (canSpawn) {
      const spawnBird = this.levels.level >= 2 && Math.random() < 0.45;
      if (spawnBird) enemies.push(new Bird(this.assets.tex.bird, 980, rand(140, 220)));
      else enemies.push(new Minion(this.assets.tex.minion, 900, 0));
      this.levels.onMinionSpawned();
      this.spawnTimer = this.spawnInterval;
    }
    for (const e of enemies) if (e instanceof Minion && e.alive) e.steerToward(pavo);
  }
}

const overlaps = (a, b) => a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;

class CollisionController {
  playerBulletsVsEnemies(playerBullets, enemies, levels, hitSfx) {
    for (const b of playerBullets) {
      if (!b.alive) continue;
      for (const e of enemies) {
        if (!e.alive) continue;
        if (overlaps(b.bounds(), e.bounds())) {
          e.hit(b.damage()); b.alive = false;
          hitSfx(0.9);
          if (!e.alive && (e instanceof Minion || e instanceof Bird)) levels.onMinionKilled();
          break;
        }
      }
    }
  }
  enemyBulletsVsPavo(enemyBullets, p) {
    if (!p.alive) return;
    for (const b of enemyBullets) {
      if (!b.alive) continue;
      if (overlaps(p.bounds(), b.bounds())) {
        b.alive = false;
        p.hp -= b.damage() > 0 ? b.damage() : 1;
        if (p.hp <= 0) { p.hp = 0; p.alive = false; }
      }
    }
  }
  enemiesVsPavo(enemies, p) {
    for (const e of enemies) if (e.alive && overlaps(p.bounds(), e.bounds())) return true;
    return false;
  }
}

// Keyboard + touch state. Mirrors InputController.handle(); "just pressed" keys are latched per frame.
class InputController {
  constructor() {
    this.down = new Set(); this.just = new Set(); this.paused = false;
    addEventListener("keydown", (e) => {
      const k = e.key.toLowerCase();
      if (["arrowleft", "arrowright", "arrowup", "arrowdown", " "].includes(k)) e.preventDefault();
      if (!this.down.has(k)) this.just.add(k);
      this.down.add(k);
    });
    addEventListener("keyup", (e) => this.down.delete(e.key.toLowerCase()));
    addEventListener("blur", () => this.down.clear());
  }
  pressed(k) { return this.down.has(k); }
  justPressed(k) { return this.just.has(k); }
  press(k) { if (!this.down.has(k)) this.just.add(k); this.down.add(k); }
  release(k) { this.down.delete(k); }
  endFrame() { this.just.clear(); }
  handle(pavo) {
    const left = this.pressed("a") || this.pressed("arrowleft");
    const right = this.pressed("d") || this.pressed("arrowright");
    if (left && !right) pavo.moveLeft(); else if (right && !left) pavo.moveRight(); else pavo.stopX();
    if (this.pressed("w") || this.pressed(" ") || this.pressed("arrowup")) pavo.jump();
    if (this.justPressed("escape") || this.justPressed("p")) this.paused = !this.paused;
  }
}

// ---------------- assets and audio ----------------
class AssetController {
  constructor(base) { this.base = base; this.tex = {}; this.music = {}; this.sfx = {}; this.current = null; this.muted = false; }
  img(name) { return new Promise((res, rej) => { const i = new Image(); i.onload = () => res(i); i.onerror = rej; i.src = `${this.base}/${name}.webp`; }); }
  async load(progress) {
    const names = ["lvOne", "lvTwo", "lvThree", "pavo", "minion", "bossy", "pavo_bullet", "boss_bullet", "bird"];
    let done = 0;
    await Promise.all(names.map(async (n) => { this.tex[n] = await this.img(n); progress(++done / (names.length + 1)); }));
    const font = new FontFace("Pixeloid", `url(${this.base}/fonts/Pixeloid.ttf)`);
    document.fonts.add(await font.load()); progress(1);
    const mk = (n, loop, vol, preload) => { const a = new Audio(`${this.base}/audio/${n}.mp3`); a.loop = loop; a.volume = vol; a.preload = preload; return a; };
    this.music = {
      1: mk("level1", true, 0.8, "auto"), 2: mk("level2", true, 0.8, "none"), 3: mk("level3", true, 0.8, "none"),
      boss: mk("boss", true, 0.8, "auto"), gameover: mk("gameover", false, 0.9, "auto"), win: mk("win", false, 0.9, "auto"),
    };
    for (const n of ["shoot", "hit", "roar"]) this.sfx[n] = mk(n, false, 1, "auto");
  }
  play(n, vol) {
    if (this.muted) return;
    const a = this.sfx[n].cloneNode(); a.volume = vol;
    a.play().catch(() => {});
  }
  stopAllMusic() { for (const m of Object.values(this.music)) { m.pause(); m.currentTime = 0; } this.current = null; }
  start(m) { this.stopAllMusic(); this.current = m; if (!this.muted) m.play().catch(() => {}); }
  playLevelMusic(level) { this.start(this.music[level < 1 || level > 3 ? 1 : level]); }
  playBossMusic() { this.start(this.music.boss); }
  playGameOverMusic() { this.start(this.music.gameover); }
  playWinMusic() { this.start(this.music.win); }
  setMuted(m) { this.muted = m; if (this.current) { if (m) this.current.pause(); else this.current.play().catch(() => {}); } }
}

// ---------------- HUD and banners ----------------
function textOutlined(g, text, x, y, size, color, { align = "left", border = 2, shadow = 1 } = {}) {
  g.font = `${size}px Pixeloid, monospace`; g.textAlign = align; g.textBaseline = "top";
  g.fillStyle = "rgba(0,0,0,.5)"; g.fillText(text, x + shadow, y + shadow);
  g.lineJoin = "round"; g.lineWidth = border * 2; g.strokeStyle = "rgba(0,0,0,.9)"; g.strokeText(text, x, y);
  g.fillStyle = color; g.fillText(text, x, y);
}

class Hud {
  draw(g, level, minions, hp, bossHP) {
    const pad = 16, size = 30, line = 36;
    textOutlined(g, "STAGE : " + level, pad, pad, size, "#fff");
    textOutlined(g, "MINIONS : " + minions, pad, pad + line, size, "#fff");
    const hpColor = hp <= 2 ? "#ff0000" : hp <= 5 ? "#ffa500" : "#32cd32";
    textOutlined(g, "HP : " + hp, WORLD_W - pad, pad, size, hpColor, { align: "right" });
    if (bossHP > 0) textOutlined(g, "FINAL BOSS HP : " + bossHP, WORLD_W - pad, pad + line, size, "#fff", { align: "right" });
  }
}

function retroBanner(g, left, leftColor, right, rightColor, glow, size, wobbleY, sub) {
  g.font = `${size}px Pixeloid, monospace`; g.textBaseline = "middle"; g.textAlign = "left";
  const wl = g.measureText(left).width, w = g.measureText(left + right).width;
  const x = (WORLD_W - w) / 2, y = WORLD_H / 2 + wobbleY;
  g.fillStyle = glow; g.globalAlpha = 0.35;
  for (let dx = -1; dx <= 1; dx++) for (let dy = -1; dy <= 1; dy++) if (dx || dy) g.fillText(left + right, x + dx * 3, y + dy * 3);
  g.globalAlpha = 1;
  g.fillStyle = "rgba(0,0,0,.8)"; g.fillText(left + right, x + 3, y + 3);
  g.lineWidth = 4; g.strokeStyle = "#000"; g.strokeText(left + right, x, y);
  g.fillStyle = leftColor; g.fillText(left, x, y);
  g.fillStyle = rightColor; g.fillText(right, x + wl, y);
  if (sub) textOutlined(g, sub, WORLD_W / 2, y + size * 0.7, 20, "#fff", { align: "center" });
}

// ---------------- game screen ----------------
const State = { PLAYING: "PLAYING", PAUSED: "PAUSED", WIN: "WIN", GAME_OVER: "GAME_OVER" };

class GameScreen {
  constructor(assets, input) {
    this.assets = assets; this.input = input;
    this.collisions = new CollisionController(); this.hud = new Hud();
    this.reset();
  }
  reset() {
    const a = this.assets;
    this.t = 0; this.bgX = 0; this.bgSpeed = 0.5; this.shakeTime = 0; this.shakeStrength = 3;
    this.pavo = new Pavo(a.tex.pavo, 40, 0);
    this.enemies = []; this.playerBullets = []; this.enemyBullets = [];
    this.levels = new LevelController(); this.spawner = new Spawn(a, this.levels);
    this.boss = null; this.state = State.PLAYING; this.input.paused = false;
    this.bossMusicOn = false;
    a.playLevelMusic(1); this.lastLevelMusic = 1;
  }
  triggerGameOver() {
    if (this.state === State.GAME_OVER) return;
    this.state = State.GAME_OVER; this.bossMusicOn = false;
    this.assets.playGameOverMusic();
    if (this.pavo.hp < 0) this.pavo.hp = 0;
  }
  update(delta) {
    const a = this.assets, input = this.input, pavo = this.pavo;
    this.t += delta;
    const dt = Math.min(delta, 1 / 30);

    if ((this.state === State.GAME_OVER || this.state === State.WIN) && input.justPressed("r")) { this.reset(); return; }

    input.handle(pavo);
    if (input.paused && this.state === State.PLAYING) { this.state = State.PAUSED; a.current && a.current.pause(); }
    else if (!input.paused && this.state === State.PAUSED) { this.state = State.PLAYING; if (a.current && !a.muted) a.current.play().catch(() => {}); }

    if (this.state !== State.PLAYING) return;

    pavo.update(dt);
    this.spawner.update(dt, this.enemies, pavo);
    this.levels.advanceLevelIfCleared();
    const currentLevel = this.levels.level < 1 ? 1 : this.levels.level;
    if (!this.bossMusicOn && currentLevel !== this.lastLevelMusic) { a.playLevelMusic(currentLevel); this.lastLevelMusic = currentLevel; }

    if (this.levels.shouldSpawnBoss() && this.boss === null) {
      this.boss = new Boss(a.tex.bossy, 820, 0);
      this.levels.bossSpawned = true;
      this.enemies.push(this.boss);
      this.bossMusicOn = true;
      a.play("roar", 0.9);
      a.playBossMusic();
    }

    for (const e of this.enemies) if (e.alive) {
      if (e instanceof Boss) { e.pursue(pavo); e.maybeShoot(this.enemyBullets, a.tex.boss_bullet, pavo); }
      e.update(dt);
    }

    if (input.justPressed("f") && pavo.canShoot()) {
      this.playerBullets.push(Bullet.playerBullet(a.tex.pavo_bullet, pavo.x + (pavo.facing === 1 ? pavo.w : -8), pavo.y + pavo.h * 0.6, pavo.facing));
      pavo.didShoot();
      a.play("shoot", 0.8);
    }

    for (const b of this.playerBullets) b.update(dt);
    for (const b of this.enemyBullets) b.update(dt);

    this.collisions.playerBulletsVsEnemies(this.playerBullets, this.enemies, this.levels, (v) => a.play("hit", v));
    this.collisions.enemyBulletsVsPavo(this.enemyBullets, pavo);

    if (this.collisions.enemiesVsPavo(this.enemies, pavo)) {
      pavo.hp -= 1;
      pavo.x = Math.max(0, pavo.x - 50);
      this.shakeTime = 0.2;
    }
    if (pavo.hp <= 0) this.triggerGameOver();

    this.playerBullets = this.playerBullets.filter((b) => b.alive);
    this.enemyBullets = this.enemyBullets.filter((b) => b.alive);
    this.enemies = this.enemies.filter((e) => e.alive);

    this.bgX -= this.bgSpeed * dt;
    if (this.bgX <= -WORLD_W) this.bgX += WORLD_W;
    if (this.shakeTime > 0) this.shakeTime -= dt;

    if (this.boss !== null && !this.boss.alive && this.state !== State.WIN) {
      this.state = State.WIN; this.bossMusicOn = false;
      a.playWinMusic();
    }
  }
  render(g) {
    const a = this.assets;
    g.save();
    g.fillStyle = "#000"; g.fillRect(0, 0, WORLD_W, WORLD_H);
    if (this.shakeTime > 0) g.translate(rand(-this.shakeStrength, this.shakeStrength), rand(-this.shakeStrength, this.shakeStrength));

    const bg = this.levels.level === 3 ? a.tex.lvThree : this.levels.level === 2 ? a.tex.lvTwo : a.tex.lvOne;
    g.drawImage(bg, this.bgX, 0, WORLD_W, WORLD_H);
    g.drawImage(bg, this.bgX + WORLD_W, 0, WORLD_W, WORLD_H);

    this.pavo.render(g);
    for (const e of this.enemies) e.render(g);
    for (const b of this.playerBullets) b.render(g);
    for (const b of this.enemyBullets) b.render(g);

    const bossHP = this.boss !== null && this.boss.alive ? this.boss.hp : -1;
    this.hud.draw(g, this.levels.level, this.levels.totalKills, this.pavo.hp, bossHP);

    const wobbleY = 4 * Math.sin(this.t * 6);
    if (this.state === State.GAME_OVER) retroBanner(g, "GAME ", "#ffa500", "OVER", "#ffff00", "#ff8000", 72, wobbleY, "Press R to play again");
    else if (this.state === State.WIN) retroBanner(g, "YOU ", "#32cd32", "WIN!", "#00ff00", "#33ff66", 72, wobbleY, "Press R to play again");
    else if (this.state === State.PAUSED) retroBanner(g, "PAUS", "#00ffff", "ED", "#ffffff", "#33e6ff", 60, wobbleY, "Press P to resume");
    g.restore();
  }
}

// ---------------- boot ----------------
(async function main() {
  const canvas = document.getElementById("game");
  const g = canvas.getContext("2d");
  const fit = () => {
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    const box = canvas.parentElement.getBoundingClientRect();
    const scale = Math.min(box.width / WORLD_W, box.height / WORLD_H);
    canvas.style.width = `${Math.floor(WORLD_W * scale)}px`;
    canvas.style.height = `${Math.floor(WORLD_H * scale)}px`;
    canvas.width = Math.round(WORLD_W * scale * dpr);
    canvas.height = Math.round(WORLD_H * scale * dpr);
    g.setTransform(canvas.width / WORLD_W, 0, 0, canvas.height / WORLD_H, 0, 0);
    g.imageSmoothingQuality = "high";
  };
  addEventListener("resize", fit); fit();

  const overlay = document.getElementById("overlay"), bar = document.getElementById("bar"), startBtn = document.getElementById("start");
  const assets = new AssetController("assets");
  await assets.load((p) => { bar.style.width = `${Math.round(p * 100)}%`; });
  document.body.classList.add("ready");

  const input = new InputController();
  let screen = null, last = 0;

  const muteBtn = document.getElementById("mute");
  muteBtn.addEventListener("click", () => { assets.setMuted(!assets.muted); muteBtn.textContent = assets.muted ? "Sound off" : "Sound on"; muteBtn.setAttribute("aria-pressed", String(assets.muted)); });

  // Touch controls map onto the same keys the keyboard uses.
  for (const b of document.querySelectorAll("[data-key]")) {
    const k = b.dataset.key;
    const on = (e) => { e.preventDefault(); input.press(k); b.classList.add("on"); };
    const off = (e) => { e.preventDefault(); input.release(k); b.classList.remove("on"); };
    b.addEventListener("pointerdown", on); b.addEventListener("pointerup", off); b.addEventListener("pointercancel", off); b.addEventListener("pointerleave", off);
  }

  const start = () => {
    if (screen) return;
    overlay.hidden = true;
    screen = new GameScreen(assets, input);
    last = performance.now();
    requestAnimationFrame(frame);
    canvas.focus();
  };
  startBtn.addEventListener("click", start);
  addEventListener("keydown", (e) => { if (!screen && document.body.classList.contains("ready") && (e.key === "Enter" || e.key === " ")) { e.preventDefault(); start(); } });

  function frame(now) {
    const delta = Math.max(0, (now - last) / 1000); last = now;
    screen.update(delta);
    screen.render(g);
    input.endFrame();
    requestAnimationFrame(frame);
  }
  // Pause automatically when the tab is hidden, as a desktop window would lose focus.
  document.addEventListener("visibilitychange", () => { if (document.hidden && screen && screen.state === State.PLAYING) input.paused = true; });
  window.__pavo = { get screen() { return screen; }, input };
})();
