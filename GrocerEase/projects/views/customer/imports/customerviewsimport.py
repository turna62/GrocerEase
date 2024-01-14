from projects.views.customer.registration.register import registercustomer
from projects.views.customer.verification.verifyotp import verifyotpcustomer
from projects.views.customer.login.login import logincustomer
from projects.views.customer.homepage.home import homecustomer
from projects.views.customer.profile.myprofile import customerprofile
from projects.views.customer.logout.logout import logoutcustomer
from projects.views.customer.cart.viewcart import cart
from projects.views.customer.itemdetails.viewdetails import item_details_with_reviews,submit_review
from projects.views.customer.cart.updatecart import updatecart
from projects.views.customer.cart.deletecartitems import delete_cart_item
from projects.views.customer.checkout.checkout import checkout
from projects.views.customer.resetpassword.sendresetotp import sendcustomerresetotp
from projects.views.customer.resetpassword.verifyresetotp import verifycustomerresetotp
from projects.views.customer.resetpassword.newpassword import changecustomerpassword
from projects.views.customer.searchfilter.searchitemcategoryseller import searchitems
from projects.views.customer.shopnavbar.viewshop import viewshop
from projects.views.customer.searchfilter.filteritemsbycategory import filteritemsbycategory
from projects.views.customer.searchfilter.filteritemsbyprice import filteritemsbyprice
from projects.views.customer.sellerdetails.viewselleritems import selleritems
from projects.views.customer.favorites.viewfavs import viewfavorites
from projects.views.customer.profile.myprofile import change_customer_image
from projects.views.customer.favorites.viewfavscount import getfavoritescount
from projects.views.customer.favorites.togglefavs import togglefavorite
from projects.views.customer.voucher.vouchercode import check_voucher
from projects.views.customer.checkout.checkout import SaveUpdatedPriceView
from projects.views.customer.recommendation.favitemsrecommendation import itemsrecommendation


