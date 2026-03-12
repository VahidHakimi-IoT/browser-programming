// ─── DOM refs ────────────────────────────────────────────────────────────────
const output = document.getElementById("output")
const list   = document.getElementById("userList")
const btn    = document.getElementById("btnLoadUsers")

// ─── Helpers ─────────────────────────────────────────────────────────────────
function log(text, isError = false) {
  const line = document.createElement("span")
  line.className   = isError ? "error-line" : "log-line"
  line.textContent = text
  output.appendChild(line)
}

function clearOutput() {
  output.textContent = ""
  list.innerHTML     = ""
}

function setLoading(on) {
  btn.disabled = on
  btn.classList.toggle("loading", on)
  btn.querySelector(".btn-label").textContent = on ? "Load" : "Load Users"
}

// ─── Button handler ───────────────────────────────────────────────────────────
btn.addEventListener("click", loadUsers)

// ─── Main ─────────────────────────────────────────────────────────────────────
async function loadUsers() {
  clearOutput()
  setLoading(true)

  try {
    // Part A — fetch + parse
    const response = await fetch("https://jsonplaceholder.typicode.com/users")

    // Part C — HTTP status check
    if (!response.ok) {
      throw new Error("HTTP error " + response.status)
    }

    const users = await response.json()

    // Part A checkpoint (open DevTools → Console to see these)
    console.log("Type:", typeof users)
    console.log("Data:", users)

    // Part B + E — loop, log, and render cards
    users.forEach(function(user, index) {
      const name  = user.name
      const email = user.email
      const city  = user.address.city   // ← nested field

      // Part B: console-style log
      log(name + "  ·  " + email + "  ·  " + city)

      // Part E: card in the list
      const li        = document.createElement("li")
      li.style.animationDelay = (index * 55) + "ms"

      const nameSpan  = document.createElement("span")
      const emailSpan = document.createElement("span")
      const citySpan  = document.createElement("span")

      nameSpan.className   = "user-name"
      emailSpan.className  = "user-email"
      citySpan.className   = "user-city"

      nameSpan.textContent  = name
      emailSpan.textContent = email
      citySpan.textContent  = city

      li.append(nameSpan, emailSpan, citySpan)
      list.appendChild(li)
    })

  } catch (error) {
    // Part C/D: display error
    log("Error: " + error.message, true)
    console.error("Fetch failed:", error)
  }

  setLoading(false)
}

/*
 * Part D — testing error handling
 * Change the URL to ".../userssss" to trigger a 404.
 * The catch block will print: Error: HTTP error 404
 */
