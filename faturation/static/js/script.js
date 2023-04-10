// $(document).on("click", "#btn-add", function () {
//     var num = $("#wrapper").children().length + 1;

//     let formAdd = `

//     <div class="form-row">
//                                 <div class="form-group col-md-3">
//                                     <label for="article:${num}">${num} Nom Article </label>
//                                     <input required name="article" type="text" class="form-control" id="article:${num}">
//                                 </div>
    
//                                 <div class="form-group col-md-3">
//                                     <label for="quantite:${num}"> Quantite </label>
//                                     <input required name="quantite" type="number" min="1" step="0.1"  class="form-control" id="quantite:${num}">
//                                 </div>
    
//                                 <div class="form-group col-md-3">
//                                     <label for="prix:${num}"> Prix Unitaire </label>
//                                     <input required name="prix" type="number" min="1" step="0.1" onchange="handleChangeSingleArticle(this.id)" class="form-control" id="prix:${num}">
//                                 </div>
    
//                                 <div class="form-group col-md-3">
//                                     <label for="total-1:${num}"> Prix Total </label>
//                                     <input required name="total-1" type="number" min="1" step="0.1" readonly class="form-control"
//                                         id="total-1:${num}">
//                                 </div>
    
//                             </div>
//                     `;

//     $("#wrapper:last").append(formAdd);
//   });

//   $(document).on('click', '#btn-remove', function(){
//     $("#wrapper").children().last().remove();
// })