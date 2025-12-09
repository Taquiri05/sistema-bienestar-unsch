console.log("personal.js cargado correctamente");

// ===================== VALIDAR ACCESO =====================
const idPersonal = localStorage.getItem("rolID");
const tipoUsuario = localStorage.getItem("tipoUsuario");

if (!idPersonal || tipoUsuario !== "personal") {
  alert("No tienes acceso a esta sección");
  window.location.href = "index.html";
}

// ===================== REFERENCIAS DEL DOM =====================
const vistaDashboard = document.getElementById("vista-dashboard");
const vistaCitas = document.getElementById("vista-citas");
const vistaHistorial = document.getElementById("vista-historial");

const btnDashboard = document.getElementById("btn-dashboard");
const btnCitas = document.getElementById("btn-citas");
const btnHistorial = document.getElementById("btn-historial");

// ===================== CAMBIAR DE VISTA =====================
function cambiarVista(vista) {
  vistaDashboard.classList.add("vista-oculta");
  vistaCitas.classList.add("vista-oculta");
  vistaHistorial.classList.add("vista-oculta");

  vista.classList.remove("vista-oculta");
  vista.classList.add("vista-activa");
}

// ===================== CARGAR ESTADÍSTICAS =====================
async function cargarEstadisticas() {
  try {
    const res = await fetch(
      `http://127.0.0.1:5000/api/citas/estadisticas/personal/${idPersonal}`
    );
    const data = await res.json();

    document.getElementById("count-pendientes").textContent = data.pendientes;
    document.getElementById("count-atendidas").textContent = data.atendidas;
    document.getElementById("count-canceladas").textContent = data.canceladas;

  } catch (error) {
    console.error("Error cargando estadísticas:", error);
  }
}

// ===================== MARCAR CITA COMO ATENDIDA =====================
async function marcarComoAtendida(idCita) {
  if (!confirm("¿Marcar esta cita como ATENDIDA?")) return;

  const res = await fetch(
    `http://127.0.0.1:5000/api/citas/atender/${idCita}`,
    { method: "PUT" }
  );

  const data = await res.json();
  alert(data.msg);

  cargarCitasPendientes();
  cargarEstadisticas();
}

// ===================== CARGAR CITAS PENDIENTES =====================
async function cargarCitasPendientes() {
  try {
    vistaCitas.innerHTML = "<h2>Cargando citas...</h2>";

    const res = await fetch(
      `http://127.0.0.1:5000/api/citas/personal/${idPersonal}`
    );
    const citas = await res.json();

    vistaCitas.innerHTML = `
      <h2 class="titulo-citas">Citas Pendientes</h2>

      <table class="tabla-citas">
        <thead>
          <tr>
            <th>ID Cita</th>
            <th>ID Estudiante</th>
            <th>Fecha</th>
            <th>Hora</th>
            <th>Estado</th>
            <th>Acción</th>
          </tr>
        </thead>

        <tbody>
          ${citas
        .map(
          (c) => `
            <tr>
              <td>${c.idCita}</td>
              <td>${c.idEstudiante}</td>
              <td>${c.fechaCita}</td>
              <td>${c.horaCita}</td>
              <td class="estado-${c.estado.toLowerCase()}">${c.estado}</td>
              <td>
                ${c.estado === "Pendiente"
              ? `<button class="btn-atender" onclick="marcarComoAtendida(${c.idCita})">Atender</button>`
              : `<span style="color:gray;">—</span>`
            }
              </td>
            </tr>
          `
        )
        .join("")}
        </tbody>
      </table>
    `;
  } catch (error) {
    console.error("Error cargando citas:", error);
    vistaCitas.innerHTML = "<p>Error cargando citas</p>";
  }
}

// ===================== BUSCAR HISTORIAL POR DNI =====================
document
  .getElementById("btnBuscarHistorial")
  .addEventListener("click", async () => {
    const dni = document.getElementById("dni-buscar").value.trim();

    if (!dni) {
      alert("Ingrese un DNI válido");
      return;
    }

    const cont = document.getElementById("resultado-historial");
    cont.innerHTML = `<p>Buscando historial...</p>`;

    const res = await fetch(
      `http://127.0.0.1:5000/api/historial/buscar/${dni}`
    );
    const data = await res.json();

    if (res.status !== 200) {
      cont.innerHTML = `<p style="color:red;">${data.error}</p>`;
      return;
    }

    const est = data.estudiante;

    cont.innerHTML = `
      <div class="hist-card">
        <h3>Datos del Estudiante</h3>
        <p><strong>Nombre:</strong> ${est.nombre} ${est.apellido}</p>
        <p><strong>Código:</strong> ${est.codigo}</p>
        <p><strong>Escuela:</strong> ${est.escuela}</p>
        <p><strong>Ciclo:</strong> ${est.ciclo}</p>
      </div>

      <h3>Historial Clínico</h3>

      ${data.historial.length > 0
        ? data.historial
          .map(
            (h) => `
        <div class="historial-card">
          <p><strong>Fecha:</strong> ${h.fecha}</p>
          <p><strong>Descripción:</strong> ${h.descripcion}</p>
        </div>
      `
          )
          .join("")
        : "<p>No tiene atenciones registradas.</p>"
      }
    `;
  });

// ===================== EVENTOS DEL MENÚ =====================
btnDashboard.addEventListener("click", () => {
  cambiarVista(vistaDashboard);
  cargarEstadisticas();
});

btnCitas.addEventListener("click", () => {
  cambiarVista(vistaCitas);
  cargarCitasPendientes();
});

btnHistorial.addEventListener("click", () => {
  cambiarVista(vistaHistorial);
});

// ===================== INICIO =====================
document.addEventListener("DOMContentLoaded", () => {
  cambiarVista(vistaDashboard);
  cargarEstadisticas();
});
