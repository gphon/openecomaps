
$(document).ready(function () {
    $("#AddPOIFrame").hide();
    var link = document.createElement('a');
    link.setAttribute("href", " javascript:void(0)");
    link.setAttribute("id", "AddPOILink");
    link.setAttribute("class", "PoiAddLink");
    link.innerHTML = "POI Hinzufügen";

    var layerDiv = $(".layersDiv");
    layerDiv.append(link);

    $("#AddPOILink").click(function () {
        if ($("#AddPOIFrame").is(":visible")) {
            $("#AddPOIFrame").fadeOut();
        } else {

            //Altes IFrame bei neuladen entfernen
            var oldFrame = $("#POIAddIFrame");
            if (oldFrame.length > 0) {
                oldFrame.remove();
            }


                //Neues IFrame generieren
                var iFrame = document.createElement("iframe");
                iFrame.setAttribute("src", "http://openecomaps.de:8005/poi/form");
                iFrame.setAttribute("class", "POIAddIFrameStyle");
                iFrame.setAttribute("id", "POIAddIFrame");
                $("#AddPOIFrame").append(iFrame);
          
            $("#AddPOIFrame").fadeIn();
        }
    });

    $("#POIHideDiv").click(function () {
        $("#AddPOIFrame").fadeOut();
    });

});
