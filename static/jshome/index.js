var dept='';
firebaseSetup();
$(document).ready(function(){
    $(".departments > li").on("click", function() {
      dept = $(this)[0].innerText;
      $(".booking-module").removeClass("hide");
    });
	// Variables
	var clickedTab = $(".tabs > .active");
	var tabWrapper = $(".tab__content");
	var activeTab = tabWrapper.find(".active");
	var activeTabHeight = activeTab.outerHeight();
	
	// Show tab on page load
	activeTab.show();
	
	// Set height of wrapper on page load
	tabWrapper.height(activeTabHeight);
	
	$(".tabs > li").on("click", function() {
		
		// Remove class from active tab
		$(".tabs > li").removeClass("active");
		
		// Add class active to clicked tab
		$(this).addClass("active");
		
		// Update clickedTab variable
		clickedTab = $(".tabs .active");
		
		// fade out active tab
		activeTab.fadeOut(250, function() {
			
			// Remove active class all tabs
			$(".tab__content > li").removeClass("active");
			
			// Get index of clicked tab
			var clickedTabIndex = clickedTab.index();

			// Add class active to corresponding tab
			$(".tab__content > li").eq(clickedTabIndex).addClass("active");
			
			// update new active tab
			activeTab = $(".tab__content > .active");
			
			// Update variable
			activeTabHeight = activeTab.outerHeight();
			
			// Animate height of wrapper to new tab height
			tabWrapper.stop().delay(50).animate({
				height: activeTabHeight
			}, 500, function() {
				
				// Fade in active tab
				activeTab.delay(50).fadeIn(200);
				
			});
		});
	});
});
function firebaseSetup(){
  // create our angular module and inject firebase
  angular.module('scheduleApp', ['firebase'])
  // create our main controller and get access to firebase
  .controller('mainController', function($scope, $firebase) {

    // connect to firebase 
      var ref = new Firebase("https://patient-portal-carehack.firebaseio.com/"+dept+"days");  
      var fb = $firebase(ref);
      var syncObject = fb.$asObject();
      $scope.booked = function(day, time){
          console.log(day, time);   
      }
      // three way data binding
      syncObject.$bindTo($scope, 'days');
      $scope.reset = function() {    
          fb.$set({
            1: {
              name: 'Monday',
              slots: {
                0900: {
                  time: '9:00am',
  //              username: username, to add user data to book table
                  booked: false
                },
                0110: {
                  time: '11:00am',
                  booked: false
                }
              }
            },
            2: {
              name: 'Tuesday',
              slots: {
                0900: {
                  time: '9:00am',
                  booked: false
                },
                0110: {
                  time: '11:00am',
                  booked: false
                }
              }
            },
          3: {
              name: 'Wednesday',
              slots: {
                0900: {
                  time: '9:00am',
                  booked: false
                },
                0110: {
                  time: '11:00am',
                  booked: false
                }
              }
            },
          4: {
              name: 'Thursday',
              slots: {
                0900: {
                  time: '9:00am',
                  booked: false
                },
                0110: {
                  time: '11:00am',
                  booked: false
                }
              }
            },
          5: {
              name: 'Friday',
              slots: {
                0900: {
                  time: '9:00am',
                  booked: false
                },
                0110: {
                  time: '11:00am',
                  booked: false
                }
              }
            }
          });    

        };

  });
}
