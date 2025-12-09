document.getElementById("loginForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  console.log("=== ENVIANDO LOGIN AL BACKEND ===");

  const correo = document.getElementById("correo").value;
  const contrasena = document.getElementById("contrasena").value;

  const datos = { correo, contrasena };

  try {
    const res = await fetch("http://127.0.0.1:5000/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos)
    });

    const json = await res.json();
    console.log("Respuesta del backend:", json);

    if (!res.ok) {
      alert(json.error || "Error al iniciar sesión");
      return;
    }

    // Limpiar sesiones anteriores
    localStorage.clear();

    // Guardar sesión actual
    localStorage.setItem("idUsuario", json.idUsuario);
    localStorage.setItem("tipoUsuario", json.tipoUsuario);
    localStorage.setItem("rolID", json.rolID);

    console.log("Sesión guardada:", {
      idUsuario: json.idUsuario,
      tipoUsuario: json.tipoUsuario,
      rolID: json.rolID
    });

    // Redirecciones
    if (json.tipoUsuario === "estudiante") {
      window.location.href = "dashboard_estudiante.html";
    } else if (json.tipoUsuario === "personal") {
      window.location.href = "dashboard_personal.html";
    } else if (json.tipoUsuario === "administrador") {
      window.location.href = "dashboard_admin.html";
    }

  } catch (error) {
    console.error("Error de conexión:", error);
    alert("No se pudo conectar con el servidor");
  }
});
