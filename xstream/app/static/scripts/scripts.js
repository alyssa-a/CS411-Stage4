$(document).ready(function () {
    // show modal
    $('#show-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const showID = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (showID === 'New Show') {
            modal.find('.modal-title').text(showID)
            $('#show-form-display').removeAttr('showID')
        }

        if (content) {
            modal.find('.form-control').val(content);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $("#add-show").click(function () {
        var showName = document.getElementById("showName").value;
        var ageRating = document.getElementById("ageRating").value;
        var releaseYear = document.getElementById("releaseYear").value;
        var rating = document.getElementById("ratings").value;
        $.ajax({
            type: 'POST',
            url: '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({ showName: showName, ageRating: ageRating, releaseYear: releaseYear, ratings: rating }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#edit-show-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const showID = button.data('source') // Extract info from data-* attributes
        var parent = button.closest('tr');
        var showName = parent.find("td:eq(1)").text();
        var ageRating = parent.find("td:eq(2)").text();
        var releaseYear = parent.find("td:eq(3)").text();
        var rating = parent.find("td:eq(4)").text();

        const modal = $(this)
        modal.find('.modal-title').text('Edit Show ' + showID)
        $('#edit-show-form-display').attr('showID', showID)

        document.getElementById("editShowName").value = showName;
        document.getElementById("editAgeRating").value = ageRating;
        document.getElementById("editReleaseYear").value = releaseYear;
        document.getElementById("editRatings").value = rating;
    })

    $("#edit-show").click(function () {
        const sID = $('#edit-show-form-display').attr('showID');
        var showName = document.getElementById("editShowName").value;
        var ageRating = document.getElementById("editAgeRating").value;
        var releaseYear = document.getElementById("editReleaseYear").value;
        var rating = document.getElementById("editRatings").value;
        $.ajax({
            type: 'POST',
            url: '/edit/' + sID,
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({ showId: sID, showName: showName, ageRating: ageRating, releaseYear: releaseYear, ratings: rating }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this);
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#search-value').on('keypress', function (e) {
        if(e.which == 13) {
            $.ajax({
                type: 'POST',
                url: '/',
                success: function (res) {
                    console.log(res.response)
                },
                error: function () {
                    console.log('Error');
                }
            });
        }
    });

});