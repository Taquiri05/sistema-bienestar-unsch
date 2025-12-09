document.getElementById("registroForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  console.log("=== ENVIANDO DATOS AL BACKEND ===");

  const nombre = document.getElementById("nombre").value;
  const apellido = document.getElementById("apellido").value;
  const dni = document.getElementById("dniEst").value;
  const correo = document.getElementById("correoReg").value;
  const contrasena = document.getElementById("contrasenaReg").value;
  const tipoUsuario = document.getElementById("tipoUsuarioReg").value;

  // Datos base
  let datos = {
    nombre: nombre,
    apellido: apellido,
    dni: dni,  // 🔥 se envía siempre, va a PERFIL
    correo: correo,
    contrasena: contrasena,
    tipoUsuario: tipoUsuario
  };

  // Datos extra según tipo
  if (tipoUsuario === "estudiante") {
    datos.codigo = document.getElementById("codigoEst").value;
    datos.escuela = document.getElementById("escuelaEst").value;
    datos.ciclo = document.getElementById("cicloEst").value;
  }

  if (tipoUsuario === "personal") {
    datos.especialidad = document.getElementById("especialidadPer").value;
  }

  if (tipoUsuario === "administrador") {
    datos.area = document.getElementById("areaAdmin").value;
    datos.cargo = document.getElementById("cargoAdmin").value;
  }

  console.log("Datos enviados:", datos);

  try {
    const respuesta = await fetch("http://127.0.0.1:5000/api/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos)
    });

    const resultado = await respuesta.json();
    console.log("Respuesta del backend:", resultado);

    if (respuesta.ok) {
      alert("Usuario registrado correctamente: ID " + resultado.idUsuario);
      window.location.href = "index.html#departamento-medico";
    } else {
      alert("Error: " + resultado.error);
    }

  } catch (error) {
    console.error("Error al conectar con el backend:", error);
    alert("No se pudo conectar con el servidor");
  }
});
