// Get references to UI elements
const output = document.getElementById("output");
const statusText = document.getElementById("status");

function log(message) {
    output.textContent += message + "\n";
}

function clearOutput() {
    output.textContent = "";
}

function setStatus(text) {
    statusText.textContent = "Status: " + text;
}

/* ==========================================================
   1) ASYNC TIMEOUT
   ========================================================== */
document.getElementById("btnTimeout").onclick = function () {

    clearOutput();
    log("Start");

    // ✅ changed 2000 → 500
    setTimeout(function () {
        log("Timeout finished after 0.5 seconds");
    }, 500);

    log("End");
};


/* ==========================================================
   2) ASYNC PROMISE
   ========================================================== */
function waitOneSecond() {
    return new Promise(function (resolve) {

        // ✅ changed to 2000ms
        setTimeout(function () {
            resolve("Promise resolved after 1 second!");
        }, 2000);
    });
}

document.getElementById("btnPromise").onclick = function () {

    clearOutput();
    setStatus("Waiting (Promise)...");

    waitOneSecond().then(function (result) {
        log(result);
        setStatus("Idle");
    });
};


/* ==========================================================
   3) ASYNC / AWAIT
   ========================================================== */
async function runAwaitExample() {

    clearOutput();

    // ✅ changed text
    setStatus("Please wait, async/await running...");

    // ✅ added logs
    log("Before await");

    const result = await waitOneSecond();

    log("After await");

    log(result);

    setStatus("Idle");
}

document.getElementById("btnAwait").onclick = runAwaitExample;


/* ==========================================================
   4) ASYNC FETCH
   ========================================================== */
async function runFetchExample() {

    clearOutput();
    setStatus("Loading from API...");

    try {

        // ✅ changed ID to force error
        const response = await fetch(
            "https://jsonplaceholder.typicode.com/todos/999999"
        );

        if (!response.ok) {
            throw new Error("HTTP Error: " + response.status);
        }

        const data = await response.json();

        // ✅ changed output
        log("ID: " + data.id);
        log("Title: " + data.title);

    } catch (error) {

        log("Error: " + error.message);

    } finally {
        setStatus("Idle");
    }
}

document.getElementById("btnFetch").onclick = runFetchExample;