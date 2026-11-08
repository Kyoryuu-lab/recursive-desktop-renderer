<h1>recursive-desktop-renderer</h1>
<p>Procedural retro desktop simulation, vector iconography, and recursive window animation (Droste effect) rendered with Pygame and compiled to MP4 via OpenCV</p>

<h2>Project description</h2>
<p>This project implements an automated computer graphics rendering and video generation pipeline that simulates a vintage operating system desktop environment and produces recursive window animations:</p>
<ol>
  <li>
    <dl>
      <dt><b>Vector Desktop &amp; Icon Graphics (Pygame):</b></dt>
      <dd>Draws customized desktop UI components from geometric primitives without external bitmap assets.</dd>
      <dd>Faithfully reproduces retro office application icons (Word, Excel, PowerPoint) using layered color gradients, quadrant dividers, circular arcs, and font typography.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Kinematics &amp; Interactive State Machine:</b></dt>
      <dd>Calculates continuous cursor movement across frames to simulate realistic user trajectory toward the target application.</dd>
      <dd>Triggers collision events (<code>collidepoint</code>) upon cursor contact to initiate window instantiation and depth growth.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Recursive Window Geometry (Droste Effect):</b></dt>
      <dd><b>Quadruple Mode (<code>--mode quadruple</code>):</b> Discrete 4-tier nesting inside a bounded central coordinate area.</dd>
      <dd><b>Infinite Mode (<code>--mode infinite</code>):</b> Deep multi-tier continuous window embedding (up to depth 200) with dynamic bounding box scale reduction.</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt><b>Automated Video Synthesis (OpenCV):</b></dt>
      <dd>Streams rendered frame buffers directly to disk and compiles sequential PNG images into high-definition H.264/MP4 video files at 30 FPS.</dd>
    </dl>
  </li>
</ol>

<h2>Project files</h2>
<table>
  <tr>
    <th colspan="2">recursive-desktop-renderer</th>
  </tr>
  <tr>
    <td>main.py</td>
    <td>Central CLI orchestrator controlling animation mode, duration, framerate, and export options</td>
  </tr>
  <tr>
    <td>modules/desktop_ui.py</td>
    <td>Vector drawing engine for desktop background, taskbar, Word/Excel/PowerPoint icons, and cursor kinematics</td>
  </tr>
  <tr>
    <td>modules/window_engine.py</td>
    <td>Window frame geometry, titlebar buttons, and recursive content scaling algorithms</td>
  </tr>
  <tr>
    <td>modules/video_encoder.py</td>
    <td>OpenCV <code>VideoWriter</code> pipeline transforming frame sequences into MP4 video</td>
  </tr>
  <tr>
    <td>README.md</td>
    <td>Project documentation and structural architecture description</td>
  </tr>
  <tr>
    <td>.gitignore</td>
    <td>Exclusion rules for generated frames, MP4 video outputs, and Python caches</td>
  </tr>
</table>

<h2>Animation Modes Comparison</h2>
<table>
  <tr>
    <th>Feature</th>
    <th>Quadruple Mode</th>
    <th>Infinite Mode</th>
  </tr>
  <tr>
    <td><b>Max Recursion Depth</b></td>
    <td>4 layers</td>
    <td>200 layers</td>
  </tr>
  <tr>
    <td><b>Initial Window Area</b></td>
    <td>Centered 600&times;400 px</td>
    <td>Full screen 800&times;600 px</td>
  </tr>
  <tr>
    <td><b>Step Interval</b></td>
    <td>90 frames (3.0 seconds)</td>
    <td>60 frames (2.0 seconds)</td>
  </tr>
  <tr>
    <td><b>Visual Aesthetic</b></td>
    <td>Discrete nested application windows</td>
    <td>Continuous fractal-like Droste tunnel</td>
  </tr>
</table>

<h2>Installation and launch</h2>
<ol>
  <b>
    <li>
      <dl>
        <dt>Clone repository</dt>
        <dd>
          <code>git clone https://github.com/Kyoryuu-lab/recursive-desktop-renderer.git</code>
        </dd>
        <dd>
          <code>cd recursive-desktop-renderer</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Install dependencies</dt>
        <dd>
          <code>pip install pygame opencv-python</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Generate Infinite Recursion Video</dt>
        <dd>
          <code>python main.py --mode infinite --duration 60 --output output/infinite.mp4</code>
        </dd>
      </dl>
    </li>
  </b>
  <b>
    <li>
      <dl>
        <dt>Generate Quadruple Recursion Video</dt>
        <dd>
          <code>python main.py --mode quadruple --duration 30 --output output/quadruple.mp4</code>
        </dd>
      </dl>
    </li>
  </b>
</ol>

<h2>Example of console output (python main.py --mode infinite)</h2>
<samp>
  <p>
    ===========================================================================<br />
    &nbsp;&nbsp;RECURSIVE DESKTOP RENDERER | PYGAME &amp; OPENCV PIPELINE<br />
    ===========================================================================<br />
    [*] Starte Rendering von 1800 Frames (Modus: INFINITE)...<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Fortschritt: 300/1800 Frames generiert...<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Fortschritt: 600/1800 Frames generiert...<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Fortschritt: 900/1800 Frames generiert...<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Fortschritt: 1200/1800 Frames generiert...<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Fortschritt: 1500/1800 Frames generiert...<br />
    &nbsp;&nbsp;&nbsp;&nbsp;- Fortschritt: 1800/1800 Frames generiert...<br />
    [*] Enkodiere 1800 Frames nach 'output/animation.mp4' (800x600 @ 30 FPS)...<br />
    [+] Video-Export erfolgreich abgeschlossen: output/animation.mp4<br />
    [*] Bereinige temporaeren Frame-Ordner 'frames'...<br />
    <br />
    ===========================================================================<br />
    &nbsp;&nbsp;RENDERING &amp; ENKODIERUNG ERFOLGREICH: output/animation.mp4<br />
    ===========================================================================<br />
  </p>
