function showContent() {
    $.get(`/laporan_admin/json/${pk}`, function(data){
    let content = '';
    content += `
    <div class="top-section d-flex flex-row justify-content-between">
        <h3>${data.fields.case_name}</h3>
        <input class="btn btn-primary btn-reply" data-bs-toggle="modal" data-bs-target="#exampleModal" type="button" value="Reply">
    </div>
    <p style="margin-bottom: 3rem;">${data.fields.crime_place}</p>
    <p><b>Informer: </b><br>
        ${data.fields.name}</p>
    <p><b>Contact Person: </b><br>
        ${data.fields.phone_num}/${data.fields.email}</p>
    <p><b>Victim: </b><br>
        ${data.fields.victim_name}</p>
    <p><b>VICTIM DESCRIPTION</b></p>
    <p>${data.fields.victim_description}</p>
    <p><b>CHRONOLOGY</b></p>
    <p>${data.fields.chronology}</p>
    `;
    $('.content').html(content);
})
}

$(document).on('submit', '#form_reply', function(e) {
    e.preventDefault()
    $.ajax({
        type:"POST",
        url:"{% url 'laporan_admin:reply_laporan_user' %}",
        data:new FormData(document.querySelector("#form_reply")),
        dataType: 'json',
    })
    document.getElementById("form_reply").reset()
})

$(document).ready( function(){
  $.get(`/laporan_admin/json/${pk}`, showContent);
})