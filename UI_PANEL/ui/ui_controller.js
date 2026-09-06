// ===============================
//  LANGUAGE SWITCH
// ===============================
function setLanguage(lang) {
    console.log("Setting language:", lang);
    localStorage.setItem("sirius_language", lang);
}


// ===============================
//  CLOCK UPDATE
// ===============================
function updateClock() {
    const now = new Date();
    const timeString = now.toLocaleTimeString('sk-SK', { hour12: false });
    document.getElementById("clock").innerText = timeString;
}

setInterval(updateClock, 1000);
updateClock();


// ===============================
//  MODULE SWITCH
// ===============================
let currentModule = "none";

function selectModule(moduleName) {
    currentModule = moduleName;
    console.log("Selected module:", moduleName);
    document.getElementById("output").innerText =
        "MODULE SELECTED: " + moduleName.toUpperCase();
}


// ===============================
//  AUTOCOMPLETE – PRÍKAZY
// ===============================
const COMMANDS = [
    "echo",
    "ls",
    "dir",
    "cd",
    "pwd",
    "help",
    "clear",
    "shutdown",
    "history"
];

const inputField = document.getElementById("user-input");

// ===============================
//  AUTOCOMPLETE BOX
// ===============================
const autocompleteBox = document.createElement("div");
autocompleteBox.id = "autocomplete-box";
autocompleteBox.style.position = "absolute";
autocompleteBox.style.background = "#111";
autocompleteBox.style.color = "#0f0";
autocompleteBox.style.padding = "5px";
autocompleteBox.style.border = "1px solid #0f0";
autocompleteBox.style.display = "none";
autocompleteBox.style.zIndex = "9999";
autocompleteBox.style.fontFamily = "Consolas";
autocompleteBox.style.fontSize = "14px";

document.body.appendChild(autocompleteBox);


// ===============================
//  AUTOCOMPLETE – LOGIKA
// ===============================
inputField.addEventListener("input", () => {
    const value = inputField.value.trim().toLowerCase();

    if (!value) {
        autocompleteBox.style.display = "none";
        return;
    }

    const matches = COMMANDS.filter(cmd => cmd.startsWith(value));

    if (matches.length === 0) {
        autocompleteBox.style.display = "none";
        return;
    }

    autocompleteBox.innerHTML = "";
    matches.forEach(cmd => {
        const item = document.createElement("div");
        item.innerText = cmd;
        item.style.cursor = "pointer";
        item.style.padding = "2px 4px";

        item.onclick = () => {
            inputField.value = cmd;
            autocompleteBox.style.display = "none";
        };

        autocompleteBox.appendChild(item);
    });

    const rect = inputField.getBoundingClientRect();
    autocompleteBox.style.left = rect.left + "px";
    autocompleteBox.style.top = (rect.bottom + 2) + "px";
    autocompleteBox.style.display = "block";
});


// ===============================
//  ARROW‑UP / ARROW‑DOWN HISTÓRIA
// ===============================
let uiHistory = [];
let historyIndex = -1;

inputField.addEventListener("keydown", (e) => {

    // ARROW UP
    if (e.key === "ArrowUp") {
        e.preventDefault();

        if (uiHistory.length === 0) return;

        if (historyIndex < uiHistory.length - 1) {
            historyIndex++;
        }

        inputField.value = uiHistory[uiHistory.length - 1 - historyIndex];
        autocompleteBox.style.display = "none";
    }

    // ARROW DOWN
    if (e.key === "ArrowDown") {
        e.preventDefault();

        if (uiHistory.length === 0) return;

        if (historyIndex > 0) {
            historyIndex--;
            inputField.value = uiHistory[uiHistory.length - 1 - historyIndex];
        } else {
            historyIndex = -1;
            inputField.value = "";
        }

        autocompleteBox.style.display = "none";
    }
});


// ===============================
//  TERMINAL FARBY – LOGIKA
// ===============================
function colorizeOutput(command, output) {

    let colorClass = "term-default";

    if (command.startsWith("echo")) colorClass = "term-green";
    else if (command.startsWith("ls") || command.startsWith("dir")) colorClass = "term-blue";
    else if (command.startsWith("cd") || command.startsWith("pwd")) colorClass = "term-yellow";
    else if (command.startsWith("help") || command.startsWith("history")) colorClass = "term-cyan";
    else if (command.startsWith("clear")) colorClass = "term-magenta";
    else if (command.startsWith("shutdown")) colorClass = "term-red";

    return `<span class="${colorClass}">${output}</span>`;
}


// ===============================
//  SEND INPUT TO BACKEND
// ===============================
function sendInput() {
    const text = inputField.value.trim();
    if (!text) return;

    autocompleteBox.style.display = "none";

    // ULOŽENIE DO UI HISTÓRIE
    uiHistory.push(text);
    historyIndex = -1;

    const lang = localStorage.getItem("sirius_language") || "SK";

    const payload = {
        module: currentModule,
        text: text,
        language: lang
    };

    console.log("Sending input:", payload);

    fetch("http://localhost:8080", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Backend returned status " + response.status);
        }
        return response.json();
    })
    .then(data => {
        console.log("Backend response:", data);

        const rawOutput = JSON.stringify(data, null, 2);
        const colored = colorizeOutput(text, rawOutput);

        document.getElementById("output").innerHTML =
            "BACKEND RESPONSE:<br>" + colored;
    })
    .catch(err => {
        console.error("Fetch error:", err);

        document.getElementById("output").innerHTML =
            `<span class="term-red">ERROR:<br>${err.toString()}</span>`;
    });

    inputField.value = "";
}
