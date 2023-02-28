function getCheckedIds() {
    var checkedIds = Array();

    var checks = $('.object-row.checked');
    for (var i = 0; i < checks.length; i++) {
        checkedIds.push(parseInt($(checks[i]).data('object-id')));
    }
    return checkedIds.sort(numericComparator);
}

function getCheckedUuids() {
    var checkedUuids = Array();

    var checks = $('.object-row.checked');
    for (var i = 0; i < checks.length; i++) {
        checkedUuids.push($(checks[i]).data('uuid'));
    }
    return checkedUuids.sort();
}

function getLabeledIds(labelId) {
    var objectRowsIds = Array();
    var labeled = $(".lbl[data-id='" + labelId + "']");
    for (var i = 0; i < labeled.length; i++) {
        var id = parseInt(
            $(labeled[i]).parents('.object-row').data('object-id')
        );
        objectRowsIds.push(id);
    }

    return objectRowsIds.sort(numericComparator);
}

function getObjectRowLabels(objectId) {
    var labelIds = Array();
    var labels = $(".object-row[data-object-id='" + objectId + "']").find(
        '.lbl'
    );
    for (var i = 0; i < labels.length; i++) {
        labelIds.push(parseInt($(labels[i]).data('id')));
    }

    return labelIds.sort(numericComparator);
}

function runActionOnObjectRows(action, onSuccess) {
    var objectIds = getCheckedIds();
    jQuery.ajaxSettings.traditional = true;
    fetchPJAXContent(document.location.href, '#pjax', {
        postData: { objects: objectIds, action: action, pjax: 'true' },
        onSuccess: onSuccess,
    });
}

function unlabelObjectRows(labelId, onSuccess) {
    var objectsIds = getCheckedIds();
    var addLabel = false;

    jQuery.ajaxSettings.traditional = true;
    fetchPJAXContent(document.location.href, '#pjax', {
        postData: {
            objects: objectsIds,
            label: labelId,
            add: addLabel,
            action: 'unlabel',
            pjax: 'true',
        },
        onSuccess: onSuccess,
    });
}

function postLabelChanges(smsIds, labelId, addLabel, number, onError, onSuccess) {
    fetchPJAXContent(document.location.href, '#pjax', {
        postData: {
            objects: smsIds,
            label: labelId,
            add: addLabel,
            action: 'label',
            pjax: 'true',
            number: number,
        },
        onSuccess: function (data, textStatus) {
            recheckIds();
            if (onSuccess) {
                onSuccess();
            }
        },
        onError: onError,
    });
}

function labelObjectRows(labelId, forceRemove, onSuccess) {

    var objectRowsIds = getCheckedIds();
    var labeledIds = getLabeledIds(labelId);

    // they all have the label, so we are actually removing this label
    var addLabel = false;
    for (var i = 0; i < objectRowsIds.length; i++) {
        var found = false;
        for (var j = 0; j < labeledIds.length; j++) {
            if (objectRowsIds[i] == labeledIds[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            addLabel = true;
            break;
        }
    }

    var checkbox = $('.lbl-menu[data-id="' + labelId + '"] .glyph');
    if (checkbox.hasClass('checked-child')) {
        addLabel = true;
    }

    if (checkbox.hasClass('checked')) {
        addLabel = false;
    }

    if (forceRemove) {
        addLabel = false;
    }

    jQuery.ajaxSettings.traditional = true;
    window.lastChecked = getCheckedIds();

    if (objectRowsIds.length == 0) {
        showWarning(
            '{% trans "No rows selected" %}',
            '{% trans "Please select one or more rows before continuing." %}'
        );
        return;
    }

    postLabelChanges(objectRowsIds, labelId, addLabel, null, null, onSuccess);
}

function showPageTitle() {
    var pageTitle = document.querySelector(".page-title");
    if (pageTitle) {
        pageTitle.classList.remove('hidden');
    }

}

function hidePageTitle() {
    var pageTitle = document.querySelector(".page-title");
    if (pageTitle) {
        pageTitle.classList.add('hidden');
    }

}

/**
 * When we refresh the object list via pjax, we need to re-select the object rows that were previously selected
 */
function recheckIds() {
    
    if (window.lastChecked && window.lastChecked.length > 0) {
        for (var i = 0; i < window.lastChecked.length; i++) {
            var row = $(".object-row[data-object-id='" + window.lastChecked[i] + "']");
            row.addClass('checked');
            row.find('temba-checkbox').attr('checked', true);
        }
        $('.search-details').hide();
        $('.list-buttons-container').addClass('visible');
        hidePageTitle();
        updateLabelMenu();
    } else {
        $('.search-details').show();
        $('.list-buttons-container').removeClass('visible');
        showPageTitle();
    }
}

function clearLabelMenu() {
    // remove all checked and partials
    $('.lbl-menu .glyph')
        .removeClass('checked')
        .removeClass('partial')
        .removeClass('checked-child');
}

// updates our label menu according to the currently selected set
function updateLabelMenu() {
    clearLabelMenu();

    var objectRowsIds = getCheckedIds();
    var updatedLabels = Object();

    for (var i = 0; i < objectRowsIds.length; i++) {
        var labelIds = getObjectRowLabels(objectRowsIds[i]);

        for (var j = 0; j < labelIds.length; j++) {
            var labelId = labelIds[j];

            if (!updatedLabels[labelId]) {
                var labeledIds = getLabeledIds(labelId);
                var objectRowIdsWithLabel = intersect(
                    objectRowsIds,
                    labeledIds
                );

                var label = $('.lbl-menu[data-id="' + labelId + '"] .glyph');

                if (objectRowIdsWithLabel.length == objectRowsIds.length) {
                    label.addClass('checked');
                    label.removeClass('partial');

                    var parentLabel = $(
                        $('.lbl-menu[data-id="' + labelId + '"]')
                            .parents('.dropdown-submenu')
                            .find('.lbl-menu')[0]
                    );
                    if (parentLabel) {
                        var parentBox = $(parentLabel.children('.glyph')[0]);
                        if (!parentBox.hasClass('checked')) {
                            parentBox.addClass('checked-child');
                        }
                    }
                } else {
                    label.addClass('partial');

                    var parentLabel = $(
                        $('.lbl-menu[data-id="' + labelId + '"]')
                            .parents('.dropdown-submenu')
                            .find('.lbl-menu')[0]
                    );
                    if (parentLabel) {
                        var parentBox = $(parentLabel.children('.glyph')[0]);
                        if (!parentBox.hasClass('checked')) {
                            parentBox.addClass('checked-child');
                        }
                    }
                }
                updatedLabels[labelId] = true;
            }
        }
    }
}

function handleRowSelection(checkbox) {
    var row = checkbox.parentElement.parentElement.classList;
    var listButtons = document.querySelector(
        '.list-buttons-container'
    ).classList;

    if (checkbox.checked) {
        row.add('checked');
    } else {
        row.remove('checked');
    }

    if (document.querySelector('tr.checked')) {
        listButtons.add('visible');
        hidePageTitle();
    } else {
        listButtons.remove('visible');
        showPageTitle();
    }

    updateLabelMenu();
}

function handleRowSelections(row) {
    var row = $(row).parent('tr');

    // noop if the row doesn't have a checkbox
    var checkbox = row.find('temba-checkbox');
    if (checkbox.length == 0) {
        return;
    }

    if (checkbox.attr('checked')) {
        row.removeClass('checked');

        var checks = $('.object-row.checked');
        if (checks.length == 0) {
            $('.list-buttons-container').removeClass('visible');
            showPageTitle();
        } else {
            $('.list-buttons-container').addClass('visible');
        }
    } else {
        $('.list-buttons-container').addClass('visible');
        row.addClass('checked');
        hidePageTitle();
    }
    updateLabelMenu();
}

function wireActionHandlers() {
    $('.page-content').on('click', '.object-btn-label', function () {
        labelObjectRows($(this).data('id'), false, wireTableListeners);
    });

    if ($('.object-btn-unlabel').length > 0) {
        if (current_label_id) {
            $('.page-content').on('click', '.object-btn-unlabel', function () {
                labelObjectRows(current_label_id, true, wireTableListeners);
            });
        }
    }

    $('.page-content').on('click', '.object-btn-restore', function () {
        runActionOnObjectRows('restore', wireTableListeners);
    });

    $('.page-content').on('click', '.object-btn-archive', function () {
        runActionOnObjectRows('archive', wireTableListeners);
    });

    $('.page-content').on('click', '.object-btn-delete', function () {
        runActionOnObjectRows('delete', wireTableListeners);
    });

    $('.page-content').on('click', '.object-btn-resend', function () {
        runActionOnObjectRows('resend', wireTableListeners);
    });

    $('.page-content').on('click', '.object-btn-close', function () {
        runActionOnObjectRows('close', wireTableListeners);
    });

    $('.page-content').on('click', '.object-btn-reopen', function () {
        runActionOnObjectRows('reopen', wireTableListeners);
    });
}

$(document).ready(function () {
    wireActionHandlers();
});
