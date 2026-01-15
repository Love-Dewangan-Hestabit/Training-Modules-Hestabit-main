let todos = [];

const titleInput = document.getElementById("todo-title");
const descInput = document.getElementById("todo-desc");
const addBtn = document.getElementById("Task-btn");
const pendingList = document.getElementById("pending-list");
const completedList = document.getElementById("completed-list");

function logError(error, place) {
  console.error("Error in:", place);
  console.error(error);
}

function saveTodos() {
  try {
    localStorage.setItem("todos", JSON.stringify(todos));
  } catch (error) {
    logError(error, "saveTodos");
  }
}

function loadTodos() {
  try {
    const data = localStorage.getItem("todos");
    todos = data ? JSON.parse(data) : [];
  } catch (error) {
    logError(error, "loadTodos");
    todos = [];
  }
}

function renderTodos() {
  pendingList.innerHTML = "";
  completedList.innerHTML = "";

  todos.forEach((todo) => {
    const li = document.createElement("li");
    li.className = "todo-item";
    if (todo.completed) li.classList.add("completed");

    const header = document.createElement("div");
    header.className = "todo-header";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = todo.completed;
    checkbox.onchange = () => toggleComplete(todo.id);

    const title = document.createElement("span");
    title.className = "todo-title";
    title.textContent = todo.title;

    const actions = document.createElement("div");
    actions.className = "actions";

    const editBtn = document.createElement("button");
    editBtn.textContent = "Edit";
    editBtn.onclick = () => editTodo(todo.id);

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.onclick = () => deleteTodo(todo.id);

    const toggle = document.createElement("button");
    toggle.textContent = todo.expanded ? "v" : ">";
    toggle.onclick = () => toggleAccordion(todo.id);

    actions.append(editBtn, deleteBtn, toggle);
    header.append(checkbox, title, actions);

    const desc = document.createElement("div");
    desc.className = "todo-desc";
    desc.textContent = todo.description || "";
    if (todo.expanded) desc.classList.add("show");

    li.append(header, desc);

    todo.completed
      ? completedList.appendChild(li)
      : pendingList.appendChild(li);
  });
}

function addTodo() {
  const title = titleInput.value.trim();
  if (!title) return;

  todos.push({
    id: Date.now(),
    title: title,
    description: descInput.value.trim(),
    completed: false,
    expanded: false,
  });

  titleInput.value = "";
  descInput.value = "";

  saveTodos();
  renderTodos();
}

function deleteTodo(id) {
  todos = todos.filter((t) => t.id !== id);
  saveTodos();
  renderTodos();
}

function editTodo(id) {
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].id === id) {
      let newTitle = prompt("Edit title:", todos[i].title);
      if (!newTitle) return;

      let newDesc = prompt("Edit description:", todos[i].description);

      todos[i].title = newTitle;
      todos[i].description = newDesc;
      break;
    }
  }

  saveTodos();
  renderTodos();
}

function toggleComplete(id) {
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].id === id) {
      if (todos[i].completed === true) {
        todos[i].completed = false;
      } else {
        todos[i].completed = true;
      }
      break;
    }
  }

  saveTodos();
  renderTodos();
}

function toggleAccordion(id) {
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].id === id) {
      if (todos[i].expanded === true) {
        todos[i].expanded = false;
      } else {
        todos[i].expanded = true;
      }
      break;
    }
  }

  saveTodos();
  renderTodos();
}

addBtn.addEventListener("click", addTodo);
titleInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") addTodo();
});

loadTodos();
renderTodos();
