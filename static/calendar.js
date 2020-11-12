var calendar = null;

document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  if (window.innerWidth > 768){
    calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: ['list', 'dayGrid', 'timeGrid', 'googleCalendar'],
      locale: 'zh-tw',
      defaultView: 'dayGridMonth',
      header: {
        left: 'listMonth, dayGridMonth, timeGridWeek',
        center: 'title',
        right: 'today, prev, next'
      },
      googleCalendarApiKey: 'AIzaSyBJWGn9l4E1JjC8wSyPMXRigqiL9nqGGhk',
      events: {
        googleCalendarId: 'frgtm4vbs1i1n8vk57ducpa4n0@group.calendar.google.com',
        className: 'gcal-event'
      },
      businessHours: [
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '09:00',
        endTime: '12:30'
      },
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '17:00',
        endTime: '20:30'
      }]
    });
  }
  else if (window.innerWidth > 576) {
    calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: ['list', 'dayGrid', 'timeGrid', 'googleCalendar'],
      locale: 'zh-tw',
      defaultView: 'timeGridDay',
      header: {
        left: 'listMonth, timeGridDay',
        center: 'title',
        right: 'today, prev, next'
      },
      googleCalendarApiKey: 'AIzaSyBJWGn9l4E1JjC8wSyPMXRigqiL9nqGGhk',
      events: {
        googleCalendarId: 'frgtm4vbs1i1n8vk57ducpa4n0@group.calendar.google.com',
        className: 'gcal-event'
      },
      businessHours: [
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '09:00',
        endTime: '12:30'
      },
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '17:00',
        endTime: '20:30'
      }]
    });
  }
  else{
    calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: ['list', 'dayGrid', 'timeGrid', 'googleCalendar'],
      locale: 'zh-tw',
      defaultView: 'timeGridDay',
      header: {
        left: 'title',
        right: 'today, prev, next'
      },
      googleCalendarApiKey: 'AIzaSyBJWGn9l4E1JjC8wSyPMXRigqiL9nqGGhk',
      events: {
        googleCalendarId: 'frgtm4vbs1i1n8vk57ducpa4n0@group.calendar.google.com',
        className: 'gcal-event'
      },
      businessHours: [
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '09:00',
        endTime: '12:30'
      },
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '17:00',
        endTime: '20:30'
      }]
    });
  }
  calendar.render();
});

function calendarSize() {
  calendar.destroy();
  var calendarEl = document.getElementById('calendar');
  if (window.innerWidth > 768){
    calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: ['list', 'dayGrid', 'timeGrid', 'googleCalendar'],
      locale: 'zh-tw',
      defaultView: 'dayGridMonth',
      header: {
        left: 'listMonth, dayGridMonth, timeGridWeek',
        center: 'title',
        right: 'today, prev, next'
      },
      googleCalendarApiKey: 'AIzaSyBJWGn9l4E1JjC8wSyPMXRigqiL9nqGGhk',
      events: {
        googleCalendarId: 'frgtm4vbs1i1n8vk57ducpa4n0@group.calendar.google.com',
        className: 'gcal-event'
      },
      businessHours: [
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '09:00',
        endTime: '12:30'
      },
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '17:00',
        endTime: '20:30'
      }]
    });
  }
  else if (window.innerWidth > 576) {
    calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: ['list', 'dayGrid', 'timeGrid', 'googleCalendar'],
      locale: 'zh-tw',
      defaultView: 'timeGridDay',
      header: {
        left: 'listMonth, timeGridDay',
        center: 'title',
        right: 'today, prev, next'
      },
      googleCalendarApiKey: 'AIzaSyBJWGn9l4E1JjC8wSyPMXRigqiL9nqGGhk',
      events: {
        googleCalendarId: 'frgtm4vbs1i1n8vk57ducpa4n0@group.calendar.google.com',
        className: 'gcal-event'
      },
      businessHours: [
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '09:00',
        endTime: '12:30'
      },
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '17:00',
        endTime: '20:30'
      }]
    });
  }
  else{
    calendar = new FullCalendar.Calendar(calendarEl, {
      plugins: ['list', 'dayGrid', 'timeGrid', 'googleCalendar'],
      locale: 'zh-tw',
      defaultView: 'timeGridDay',
      header: {
        left: 'title',
        right: 'today, prev, next'
      },
      googleCalendarApiKey: 'AIzaSyBJWGn9l4E1JjC8wSyPMXRigqiL9nqGGhk',
      events: {
        googleCalendarId: 'frgtm4vbs1i1n8vk57ducpa4n0@group.calendar.google.com',
        className: 'gcal-event'
      },
      businessHours: [
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '09:00',
        endTime: '12:30'
      },
      {
        daysOfWeek: [1, 2, 3, 4, 5],
        startTime: '17:00',
        endTime: '20:30'
      }]
    });
  }
  calendar.render();
}

