function loadFileList() {
  const ul = document.getElementById("notebook-list");
  
  if (window.htmlFiles && window.htmlFiles.length > 0) {
    ul.innerHTML = "";
    window.htmlFiles.forEach(file => {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = file;
      a.textContent = file;
      li.appendChild(a);
      ul.appendChild(li);
    });
  } else {
    ul.innerHTML = "<li>No HTML files found.</li>";
  }
}

document.addEventListener('DOMContentLoaded', loadFileList);
