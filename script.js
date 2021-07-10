var statisticLine = document.querySelector('.statistic__line');
var clientsNowSecond = document.querySelector('.clients__now_second');

statisticLine.style.width = clientsNowSecond.textContent*10 + "%";