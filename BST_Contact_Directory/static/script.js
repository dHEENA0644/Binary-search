const API_URL = "http://127.0.0.1:5000";

async function addContact() {
  const name = document.getElementById("name").value;
  const phone = document.getElementById("phone").value;
  const email = document.getElementById("email").value;

  if (!name || !phone || !email) {
    alert("Please fill all fields!");
    return;
  }

  const res = await fetch(`${API_URL}/add`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ name, phone, email })
  });

  const data = await res.json();
  alert(data.message);
  loadContacts();
}

async function searchContact() {
  const name = document.getElementById("name").value;
  if (!name) return alert("Enter a name to search");

  const res = await fetch(`${API_URL}/search/${name}`);
  const data = await res.json();

  if (res.ok) {
    alert(`Found:\nName: ${data.name}\nPhone: ${data.phone}\nEmail: ${data.email}`);
  } else {
    alert(data.error);
  }
}

async function deleteContact() {
  const name = document.getElementById("name").value;
  if (!name) return alert("Enter a name to delete");

  const res = await fetch(`${API_URL}/delete/${name}`, { method: "DELETE" });
  const data = await res.json();
  alert(data.message);
  loadContacts();
}

async function loadContacts() {
  const res = await fetch(`${API_URL}/all`);
  const data = await res.json();
  const tbody = document.querySelector("#contactTable tbody");
  tbody.innerHTML = "";

  data.forEach(c => {
    const row = `<tr><td>${c.name}</td><td>${c.phone}</td><td>${c.email}</td></tr>`;
    tbody.innerHTML += row;
  });
}

window.onload = loadContacts;
