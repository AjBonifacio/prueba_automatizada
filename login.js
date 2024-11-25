const loginForm = document.getElementById('loginForm');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const errorMessage = document.getElementById('errorMessage');
const gestionEstudiantes = document.getElementById('gestionEstudiantes');
const addEstudianteButton = document.getElementById('addEstudiante');

const usuarioCorrecto = 'angelo';
const contrasenaCorrecta = 'boni05';

loginForm.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevenir que el formulario se envíe

  const username = usernameInput.value;
  const password = passwordInput.value;

  if (username === usuarioCorrecto && password === contrasenaCorrecta) {
    // Si las credenciales son correctas, mostrar la gestión de estudiantes
    gestionEstudiantes.style.display = 'block';
    loginForm.style.display = 'none'; // Ocultar el formulario de login
  } else {
    // Si las credenciales son incorrectas, mostrar el mensaje de error
    errorMessage.style.display = 'block';
  }
});

addEstudianteButton.addEventListener('click', function() {
  const Matricula = document.getElementById('Matricula').value;
  const Nombre = document.getElementById('Nombre').value;
  const Apellidos = document.getElementById('Apellidos').value;
  const Materia = document.getElementById('Materia').value;
  const Nota = document.getElementById('Nota').value;
  const listaEstudiantes = document.getElementById("listaEstudiantes");

  if (Matricula && Nombre && Apellidos && Materia && Nota) {
    const newFila = document.createElement('tr');
    newFila.innerHTML = `
      <td>${Matricula}</td>
      <td>${Nombre}</td>
      <td>${Apellidos}</td>
      <td>${Materia}</td>
      <td>${Nota}</td>
    `;

    // Crear el botón de borrar
    let borrar = document.createElement('button');
    borrar.textContent = 'Borrar';
    borrar.addEventListener('click', () => {
      listaEstudiantes.removeChild(newFila); // Corregido aquí
    });

    // Crear el botón de editar 
    let editar = document.createElement('button');
    editar.textContent = 'Editar';
    editar.addEventListener('click', () => {
      if (editar.textContent === 'Editar') {
        // Colocar los datos de la fila en los inputs para editarlos
        document.getElementById('Matricula').value = newFila.children[0].textContent;
        document.getElementById('Nombre').value = newFila.children[1].textContent;
        document.getElementById('Apellidos').value = newFila.children[2].textContent;
        document.getElementById('Materia').value = newFila.children[3].textContent;
        document.getElementById('Nota').value = newFila.children[4].textContent;

        // Cambiar el texto del botón a "Guardar"
        editar.textContent = 'Guardar';
      } else if (editar.textContent === 'Guardar') {
        // Guardar los cambios y actualizar la fila
        newFila.children[0].textContent = document.getElementById('Matricula').value;
        newFila.children[1].textContent = document.getElementById('Nombre').value;
        newFila.children[2].textContent = document.getElementById('Apellidos').value;
        newFila.children[3].textContent = document.getElementById('Materia').value;
        newFila.children[4].textContent = document.getElementById('Nota').value;

        editar.textContent = 'Editar';

        // Limpiar los campos después de guardar
        document.getElementById('Matricula').value = '';
        document.getElementById('Nombre').value = '';
        document.getElementById('Apellidos').value = '';
        document.getElementById('Materia').value = '';
        document.getElementById('Nota').value = '';
      }
    });

    // Agregar los botones de editar y borrar a la fila
    let accionEditar = document.createElement('td');
    accionEditar.appendChild(editar);

    let accionBorrar = document.createElement('td');
    accionBorrar.appendChild(borrar);

    // Añadir los botones a la fila
    newFila.appendChild(accionBorrar);
    newFila.appendChild(accionEditar);

    // Añadir la fila a la tabla
    listaEstudiantes.appendChild(newFila);

    // Limpiar los campos después de agregar un estudiante
    document.getElementById('Matricula').value = '';
    document.getElementById('Nombre').value = '';
    document.getElementById('Apellidos').value = '';
    document.getElementById('Materia').value = '';
    document.getElementById('Nota').value = '';
  } else {
    alert("Por favor, ingresa todos los campos.");
  }
});
