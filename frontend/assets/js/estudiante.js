const API = "http://127.0.0.1:5000/api";


// =========================
//   CAMBIAR VISTAS
// =========================
document.getElementById("btn-dashboard").onclick = () => {
  mostrarVista("vista-dashboard");
  cargarEstadisticas();
};

document.getElementById("btn-reservar").onclick = () => mostrarVista("vista-reservar");

document.getElementById("btn-mis-citas").onclick = () => {
  mostrarVista("vista-mis-citas");
  cargarCitas();
};

function mostrarVista(id) {
  document.querySelectorAll("section").forEach(s => s.classList.add("vista-oculta"));
  document.getElementById(id).classList.remove("vista-oculta");
}



// =========================
//   RESERVAR CITA
// =========================
document.getElementById("form-reserva").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    idEstudiante: localStorage.getItem("rolID"),   // 🔥 CORREGIDO
    especialidad: document.getElementById("especialidad").value,
    fechaCita: document.getElementById("fecha").value,
    horaCita: document.getElementById("hora").value
  };

  const res = await fetch(`${API}/citas/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const json = await res.json();
  alert(json.msg);

  cargarEstadisticas();
  cargarCitas();
});



// =========================
//   LISTAR CITAS
// =========================
async function cargarCitas() {
  const idEstudiante = localStorage.getItem("rolID");  // 🔥 CORREGIDO

  if (!idEstudiante) {
    alert("ERROR: No hay estudiante en sesión.");
    return;
  }

  const res = await fetch(`${API}/citas/estudiante/${idEstudiante}`);
  const citas = await res.json();

  const tabla = document.getElementById("tabla-citas");
  tabla.innerHTML = "";

  citas.forEach(c => {
    tabla.innerHTML += `
            <tr>
                <td>${c.especialidad}</td>
                <td>${c.fechaCita}</td>
                <td>${c.horaCita}</td>
                <td>${c.estado}</td>
                <td>
                    <button class="btn-cancelar" onclick="cancelarCita(${c.idCita})">
                        Cancelar
                    </button>
                </td>
            </tr>
        `;
  });
}



// =========================
//   CANCELAR CITA
// =========================
async function cancelarCita(idCita) {
  if (!confirm("¿Seguro que deseas cancelar esta cita?")) return;

  const res = await fetch(`${API}/citas/${idCita}`, {
    method: "DELETE"
  });

  const json = await res.json();
  alert(json.msg);

  cargarCitas();
  cargarEstadisticas();
}



// =========================
//   ESTADÍSTICAS DEL DASHBOARD
// =========================
async function cargarEstadisticas() {
  const id = localStorage.getItem("rolID");  // 🔥 CORREGIDO
  if (!id) return;

  const res = await fetch(`${API}/citas/estadisticas/${id}`);
  const data = await res.json();

  document.getElementById("count-programadas").innerText = data.programadas;
  document.getElementById("count-atendidas").innerText = data.atendidas;
  document.getElementById("count-canceladas").innerText = data.canceladas;
}

cargarEstadisticas();
