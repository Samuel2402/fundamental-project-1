from application import db
from application.models import Store, Receipts

db.drop_all()
db.create_all()

#adding store to db
mcdonalds_newbury = Store(shop_name='McDonalds', shop_address='63 Northbrook st', shop_postcode='RG14 1AE', takeaway=True)
tesco_newbury_superstore1 = Store(shop_name='Tesco', shop_address='London rd, Newbury', shop_postcode='RG14 2BP', takeaway=False)
#adding receipts to db
receipt1 = Receipts(most_expensive=5.09, cost_of_alcohol=0, date_of_reciept='2021/06/23', receipt_total=11.36, takeaway=True, delivery_fee=1.99, delivery_time_mins=28, store=mcdonalds_newbury)
receipt2 = Receipts(most_expensive=2.80, cost_of_alcohol=16, date_of_reciept='2021/03/15', receipt_total=11.90, store=tesco_newbury_superstore1)
receipt3 = Receipts(most_expensive=3.00, cost_of_alcohol=0, date_of_reciept='2021/05/03', receipt_total=18.76, store=tesco_newbury_superstore1)
receipt4 = Receipts(most_expensive=2.00, cost_of_alcohol=0, date_of_reciept='2021/01/02', receipt_total=20.91, store=tesco_newbury_superstore1)

store_list = [mcdonalds_newbury, tesco_newbury_superstore1]
receipt_list = [receipt1, receipt2, receipt3, receipt4]

for i in store_list:
    db.session.add(i)
for i in receipt_list:
    db.session.add(i)
db.session.commit()

############################### Stats_for_nerds #########################################

########################### table info Shopping_stats ###################################

#store_receipt_list = [receipt1.store, receipt2.store, receipt3.store, receipt4.store]

#def mcdonalds_newbury_stats():
#    count=0
#    for store in store_receipt_list:
#        where store = mcdonalds_newbury:
#            count += recreceipt_total
#            return count
#       else:
#            return count

#def tesco_newbury_superstore1():
#    count=0
#    for i in store_receipt_list:
#        where i = tesco_newbury_superstore1:
#            count += receipt_total
#            return count
#        else:
#            return count


#stats_mcdonalds_newbury = Shopping_stats(total_spent=count)
#stats_tesco_newbury_superstore1 = Shopping_stats(total_spent=count) 

#db.session.add(stats_mcdonalds_newbury)
#db.session.add(stats_tesco_newbury_superstore1)
#db.session.commit()


##################################### old ################################################

#stores
#db.session.add(mcdonalds_newbury)
#db.session.add(tesco_newbury_superstore1)
#receipts
#db.session.add(receipt1)

#first_receipt = Receipts.query.first()
#print(first_receipt)


stats_mcdonalds_newbury = [receipt1.most_expensive, receipt2.most_expensive, receipt3.most_expensive, receipt4.most_expensive]
stats_tesco_newbury_superstore1 = [receipt1.receipt_total, receipt2.receipt_total, receipt3.receipt_total, receipt4.receipt_total]

#def most_exp_list():
#    list = sorted(most_exp_list, reverse=True)
      
#def total_spent():
#    list = receipt_total_list
#    count=0
#    for i in list:
#        count = count + list[i]
#        return count 
#    else: 
#        return count