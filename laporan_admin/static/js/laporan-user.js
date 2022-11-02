function showContent() {
    $.get('/laporan-admin/json/', function(data){
    let content = '';
    for (let i=0; i<data.length; i++){
    let chronology = `${data[i].fields.chronology}`
    chronology = chronology.slice(0,40)+ "..."
    content += `
    <tr style="cursor: pointer;">
        <td class="text-center"><input type="checkbox" class="checkbox"></td>
        <td class="text-center">${data[i].fields.name}</td>
        <td class="text-center">${data[i].fields.case_name}</td>
        <td class="text-center">${data[i].fields.crime_place}</td>
        <td class="text-center">${chronology}</td>
        <td class="text-center">
            <form action="/laporan-admin/details/${data[i].pk}" style="padding: 0; box-shadow: none;" method = "GET">{% csrf_token %}
                <input type="image" src="{% static 'image/btn-eye.png' %}" onmouseover="this.src='{% static 'image/btn-eye-hover.png' %}';" onmouseout="this.src='{% static 'image/btn-eye.png' %}';" style="width: 30px; height: 30px; padding:0;">
            </form>
        </td>
        <td class="text-center">
            <input type="image" src="{% static 'image/btn-delete.png' %}" onmouseover="this.src='{% static 'image/btn-delete-hover.png' %}';" onmouseout="this.src='{% static 'image/btn-delete.png' %}';" onclick="deleteRow(${data[i].pk})" style="width: 30px; height: 30px; padding: 0;"/>
        </td>
    </tr>
    `;
    $('.content').html(content);
    }
})
}

function deleteRow(id) {
  $.ajax({
        type: 'DELETE',
        url: `/laporan-admin/delete/`,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
        },
        success: function(data) {
            $.get("/laporan-admin/json/", showContent);
        },
    });
}

function openDetail(id) {
    $.ajax({
        type: 'POST',
        url: `/laporan-admin/detail/${id}/`,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
        },
    });
}

$(document).ready( function(){
  $.get("/laporan-admin/json/", showContent);
})