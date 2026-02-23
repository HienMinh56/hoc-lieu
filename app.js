const toggleButton = document.getElementById("toggle-btn");
const sidebar = document.getElementById("sidebar");

function toggleSidebar() {
  sidebar.classList.toggle("close");
  toggleButton.classList.toggle("rotate");

  closeAllSubMenus();
}

function toggleSubMenu(button) {
  if (!button.nextElementSibling.classList.contains("show")) {
    closeAllSubMenus();
  }

  button.nextElementSibling.classList.toggle("show");
  button.classList.toggle("rotate");

  if (sidebar.classList.contains("close")) {
    sidebar.classList.toggle("close");
    toggleButton.classList.toggle("rotate");
  }
}

function closeAllSubMenus() {
  Array.from(sidebar.getElementsByClassName("show")).forEach((ul) => {
    ul.classList.remove("show");
    ul.previousElementSibling.classList.remove("rotate");
  });
}

// ===== CODE EDITOR FUNCTIONS =====

// Tab switching function for F9
function openTab(evt, tabId) {
  // Hide all tab contents
  const tabContents = document.getElementsByClassName("tab-content");
  for (let i = 0; i < tabContents.length; i++) {
    tabContents[i].classList.remove("active");
  }

  // Remove active class from all tab buttons in the same container
  const container = evt.currentTarget.closest(".code-tabs");
  const tabBtns = container.getElementsByClassName("tab-btn");
  for (let i = 0; i < tabBtns.length; i++) {
    tabBtns[i].classList.remove("active");
  }

  // Show the current tab and add active class to the button
  document.getElementById(tabId).classList.add("active");
  evt.currentTarget.classList.add("active");
}

// Tab switching function for F10
function openTabF10(evt, tabId) {
  // Hide all F10 tab contents
  const tabContents = document.getElementsByClassName("tab-content-f10");
  for (let i = 0; i < tabContents.length; i++) {
    tabContents[i].classList.remove("active");
  }

  // Remove active class from all tab buttons in the same container
  const container = evt.currentTarget.closest(".code-tabs");
  const tabBtns = container.getElementsByClassName("tab-btn");
  for (let i = 0; i < tabBtns.length; i++) {
    tabBtns[i].classList.remove("active");
  }

  // Show the current tab and add active class to the button
  document.getElementById(tabId).classList.add("active");
  evt.currentTarget.classList.add("active");
}

// Pyodide instance
let pyodide = null;
let pyodideLoading = false;

// Load Pyodide
async function loadPyodideInstance() {
  if (pyodide) return pyodide;

  if (pyodideLoading) {
    // Wait for existing load to complete
    while (pyodideLoading) {
      await new Promise((resolve) => setTimeout(resolve, 100));
    }
    return pyodide;
  }

  pyodideLoading = true;

  try {
    // Load Pyodide script if not already loaded
    if (typeof loadPyodide === "undefined") {
      await new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js";
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
      });
    }

    pyodide = await loadPyodide();
    return pyodide;
  } finally {
    pyodideLoading = false;
  }
}

// Run Python code
async function runPython(baiId) {
  const codeArea = document.getElementById(`code-${baiId}`);
  const outputArea = document.getElementById(`output-${baiId}`);
  const runBtn = codeArea
    .closest(".code-editor-wrapper")
    .querySelector(".run-btn");

  const code = codeArea.value;

  // Show loading state
  runBtn.classList.add("loading");
  runBtn.innerHTML = '<span class="spinner"></span> Loading...';
  outputArea.textContent = "⏳ Đang tải Pyodide...";
  outputArea.className = "code-output";

  try {
    // Load Pyodide if not already loaded
    const py = await loadPyodideInstance();

    outputArea.textContent = "⏳ Đang chạy code...";

    // Capture stdout
    py.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
    `);

    // Run the user's code
    try {
      py.runPython(code);

      // Get stdout output
      const stdout = py.runPython("sys.stdout.getvalue()");
      const stderr = py.runPython("sys.stderr.getvalue()");

      if (stderr) {
        outputArea.textContent = stderr;
        outputArea.className = "code-output error";
      } else if (stdout) {
        outputArea.textContent = stdout;
        outputArea.className = "code-output success";
      } else {
        outputArea.textContent = "✓ Code chạy thành công (không có output)";
        outputArea.className = "code-output success";
      }
    } catch (err) {
      outputArea.textContent = "❌ Lỗi: " + err.message;
      outputArea.className = "code-output error";
    }

    // Reset stdout/stderr
    py.runPython(`
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
    `);
  } catch (err) {
    outputArea.textContent = "❌ Không thể tải Pyodide: " + err.message;
    outputArea.className = "code-output error";
  }

  // Reset button
  runBtn.classList.remove("loading");
  runBtn.innerHTML = `
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#fff"><path d="M320-200v-560l440 280-440 280Z"/></svg>
    Run
  `;
}

// Run Python code with input support
async function runPythonWithInput(baiId) {
  const codeArea = document.getElementById(`code-${baiId}`);
  const inputArea = document.getElementById(`input-${baiId}`);
  const outputArea = document.getElementById(`output-${baiId}`);
  const runBtn = codeArea
    .closest(".code-editor-wrapper")
    .querySelector(".run-btn");

  const code = codeArea.value;
  const inputValues = inputArea ? inputArea.value.split("\n") : [];

  // Show loading state
  runBtn.classList.add("loading");
  runBtn.innerHTML = '<span class="spinner"></span> Loading...';
  outputArea.textContent = "⏳ Đang tải Pyodide...";
  outputArea.className = "code-output";

  try {
    // Load Pyodide if not already loaded
    const py = await loadPyodideInstance();

    outputArea.textContent = "⏳ Đang chạy code...";

    // Setup input simulation and capture stdout
    const inputJSON = JSON.stringify(inputValues);
    py.runPython(`
import sys
from io import StringIO

# Store original stdout/stderr
_orig_stdout = sys.stdout
_orig_stderr = sys.stderr

# Create new StringIO for capturing
sys.stdout = StringIO()
sys.stderr = StringIO()

# Setup input simulation
_input_values = ${inputJSON}
_input_index = 0

def _custom_input(prompt=""):
    global _input_index
    print(prompt, end="")
    if _input_index < len(_input_values):
        value = _input_values[_input_index]
        _input_index += 1
        print(value)  # Echo the input
        return value
    else:
        raise EOFError("Hết input! Vui lòng thêm giá trị input.")

# Replace built-in input
__builtins__.input = _custom_input
    `);

    // Run the user's code
    try {
      py.runPython(code);

      // Get stdout output
      const stdout = py.runPython("sys.stdout.getvalue()");
      const stderr = py.runPython("sys.stderr.getvalue()");

      if (stderr) {
        outputArea.textContent = stderr;
        outputArea.className = "code-output error";
      } else if (stdout) {
        outputArea.textContent = stdout;
        outputArea.className = "code-output success";
      } else {
        outputArea.textContent = "✓ Code chạy thành công (không có output)";
        outputArea.className = "code-output success";
      }
    } catch (err) {
      // Get any output before the error
      const stdout = py.runPython("sys.stdout.getvalue()");
      let errorMsg = "❌ Lỗi: " + err.message;
      if (stdout) {
        errorMsg = stdout + "\n\n" + errorMsg;
      }
      outputArea.textContent = errorMsg;
      outputArea.className = "code-output error";
    }

    // Reset stdout/stderr
    py.runPython(`
sys.stdout = _orig_stdout
sys.stderr = _orig_stderr
    `);
  } catch (err) {
    outputArea.textContent = "❌ Không thể tải Pyodide: " + err.message;
    outputArea.className = "code-output error";
  }

  // Reset button
  runBtn.classList.remove("loading");
  runBtn.innerHTML = `
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#fff"><path d="M320-200v-560l440 280-440 280Z"/></svg>
    Run
  `;
}
