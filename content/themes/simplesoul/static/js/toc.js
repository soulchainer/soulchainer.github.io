/* Script for the main TOC of an article */
"use strict";
var toc = document.getElementById("indice-de-contenido");
var title = toc.getElementsByClassName("topic-title")[0];
var content = toc.getElementsByTagName("ul")[0];
content.setAttribute("class", content.getAttribute("class") + " hide");
title.setAttribute("class", title.getAttribute("class") + " arrowdown");
title.addEventListener("click", function () {
  var contentClass = content.getAttribute("class");
  var titleClass = title.getAttribute("class");
  if (contentClass.indexOf("hide") != -1){ // if the toc content is hidden
    // replace hide for show class to display content
    content.setAttribute("class", contentClass.replace("hide","show"));
    title.setAttribute("class", titleClass.replace("arrowdown", "arrowup"));
  } else { // the content is already showing
    // replace class show for hide to hide content
    content.setAttribute("class", contentClass.replace("show","hide"));
    title.setAttribute("class", titleClass.replace("arrowup", "arrowdown"));
  }
});
