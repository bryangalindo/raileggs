event_codes = {
    'ABNO': 'ARRIVED BUT NOT ORDERED',
    'ADRI': 'PULLED FROM THE CUSTOMER',
    'AETA': 'ADVANCED ETA',
    'AETI': 'ETA AT INTERCHANGE POINT',
    'AINV': 'INVENTORY MOVE (AAR USE ONLY)',
    'ARIL': 'ARRIVAL AT INTRANSIT LOCATION',
    'ARRI': 'ARRIVAL AT FINAL DESTINATION',
    'AVPL': 'AVAILABLE FOR PLACEMENT',
    'BADO': 'BAD ORDER',
    'BFRM': 'BAD ORDER FROM',
    'BHVY': 'BAD ORDER HEAVY-TO-REPAIR',
    'BLGT': 'BAD ORDER LIGHT-TO-REPAIR',
    'BOGD': 'BAD ORDER (SIMS)',
    'BOHR': 'BAD ORDER HOURS-TO-REPAIR',
    'BOLA': 'BILL OF LADING ENTERED BY SIMS',
    'BOLP': 'PHYSICAL BILL CREATED AT DEST',
    'BXNG': 'BOUNDARY CROSSING',
    'CGIP': 'CAR GRADE BY INSPECTION',
    'CGRD': 'CAR GRADE BY WAYBILL (AAR)',
    'CH80': 'CH RULE 5 - TERMINAL SWITCH',
    'CH81': 'CH RULE 5 - INTERMEDIAT SWITCH',
    'CH82': 'CH RULE 15 - TO DELINQUENT RD',
    'CH83': 'CH RULE 15 - TO HOLDING RD',
    'CH84': 'CH RULE 5-INTERM FOLLOW INTERM',
    'CH85': 'CH RULE 5 - TERM FOLLOW INTERM',
    'CONF': 'CONFIRMATION OF NOTIFICATION',
    'CPRQ': 'REQUEST FOR CONSTRUCTIVE PLACE',
    'DAMG': 'DAMAGE TO EQUIP WAS REPORTED',
    'DCHG': 'DATA CHANGE TO BOL',
    'DFLC': 'DEPARTED FROM LOCATION',
    'DLCM': 'OUTGATE FOR CO-MATERIAL XFER',
    'DLEL': 'OUTGATE EMPTY FOR LOAD SHIFT',
    'DLFR': 'OUTGATED FOR RETIREMENT',
    'DLLL': 'LIVE LIFT OUTGATE',
    'DLLS': 'OUTGATE LOAD FOR LOAD SHIFT',
    'DLLT': 'OUTGATE LOAD FOR LOT TRANSFER',
    'DLNR': 'OUTGATE FOR NON-REVENUE LOAD',
    'DLOF': 'OUTGATE FOR RETURN',
    'DLOV': 'OUTGATE FOR OVER THE ROAD',
    'DLRP': 'OUTGATE FOR REPAIR',
    'DLTA': 'OUTGATE FOR TURNAROUND',
    'DLTN': 'OUTGATE FOR TERMINATION',
    'DPAC': 'DEMURRAGE PLACE',
    'DPUL': 'DEMURRAGE PULL',
    'DRMP': 'DERAMPED',
    'DUMP': 'COAL DUMP MOVE (TYES EVENT)',
    'ECHG': 'EQUIPMENT CHANGE ON BOL',
    'EMAV': 'EMPTY AVAILABLE FOR USE',
    'EMDV': 'EMPTY AVAILABLE FOR USE-GRD D',
    'ENRT': 'ENROUTE',
    'EQPP': 'EQUIPMENT POSITION REPORT',
    'ERPO': 'END REPOSITION OF EMPTY EQUIP',
    'EWIP': 'EARLY WARNING INSPECTION',
    'EWLT': 'EARLY WARNING LETTER--AAR ONLY',
    'FADD': 'INVENTORY FORCE ADD',
    'FDEL': 'INVENTORY FORCE DEL',
    'FMVE': 'INVENTORY FORCE MOVE',
    'FRTK': 'FROM REPAIR TRACK',
    'HADR': 'HWY DEPART FROM RR FAC TO CUST',
    'HHAR': 'HWY ARRIVAL AT RR FAC FROM CUS',
    'HIGT': 'INTERMODAL IN-GATE INTERMEDIAT',
    'HLCK': 'HITCH LOCK CHECK',
    'HMIS': 'TO HOLD, DELAYED, MISC',
    'HOGT': 'INTERMODAL OUT-GATE INTERMEDIA',
    'HOLD': 'HOLD ORDERS PLACED ON EQUIPMNT',
    'ICHD': 'INTERCHANGE DELIVERY',
    'ICHG': 'INTERCHANGE',
    'ICHR': 'INTERCHANGE RECEIPT',
    'ICHV': 'INTERCHANGE RECORD VERIFIED',
    'ILFC': 'INTERMEDIATE LOAD ON FLATCAR',
    'INSP': 'REEFER WAS INSPECTED',
    'IRFC': 'INTERMEDIATE REMOVE FROM CAR',
    'LASN': 'LOCOMOTIVE ASSIGNED TO TRAIN',
    'LCOM': 'LAST COMMODITY',
    'LDCH': 'CONTAINER ATTACHED TO CHASSIS',
    'LDFC': 'LOADED ON FLAT CAR',
    'LDSF': 'LOAD SHIFTED FROM',
    'LDST': 'LOAD SHIFTED TO',
    'LINE': 'RELEASE TRAILER FOR CASH',
    'LTCK': 'LOT INVENTORY COMPLETED',
    'LUSN': 'LOCOMOTIVE UNASSIGNED FROM TRN',
    'MAWY': 'MOVE AWAY',
    'MNOT': 'SHIPMENT CHANGE, RENOTIFY',
    'MRLS': 'MECH RLSE TO TRANSP FOR MVMNT',
    'MURL': 'MECH UN-RLSE TO TRANSP',
    'NCHG': 'SHIPMENT NOTIFICATION CHANGE',
    'NOBL': 'NO BILL AT LOCATION',
    'NOCU': 'NOTIFIED CUSTOMS',
    'NOPA': 'NOTIFY PATRON -- EQUIP AVAIL',
    'NOTE': 'NOTIFIED VIA EDI',
    'NOTF': 'NOTIFIED VIA FAX',
    'NOTV': 'NOTIFIED VIA VOICE',
    'NTFY': 'USER GENERATED CUSTOMER NOTIFY',
    'OPRQ': 'PLACE REQUEST (CSAO)',
    'ORPL': 'ORDERED FOR PLACEMENT',
    'OSTH': 'FROM STORAGE,HOLD,DELAYED,MISC',
    'PACT': 'PLACEMENT - ACTUAL',
    'PCON': 'PLACEMENT - CONSTRUCTIVE',
    'PFLT': 'PULL FROM LEASED TRACK',
    'PFPS': 'CAR PULLED FROM PATRON SIDING',
    'PLJI': 'PLACED AT JOINT INDUSTRY',
    'PLLF': 'PLACED LOAD TO LT FOR FORWARDI',
    'PLLT': 'PLACED TO LEASED TRACK',
    'PLMC': 'PLACED AT MIXING CENTER (TYES)',
    'PLRM': 'PLACED AT PIGGYBACK FACILITY',
    'PUJI': 'PULLED FROM JOINT INDUSTRY',
    'PULL': 'PULLED FOR SHIPMENT',
    'PUMC': 'PULLED FR MIXING CENTER (TYES)',
    'PURM': 'PULLED FROM PIGGYBACK FACILITY',
    'PURQ': 'PULL REQUEST (CSAO)',
    'RAMP': 'RAMPED',
    'RCCM': 'INGATE FOR CO-MATERIAL XFER',
    'RCEL': 'INGATE EMPTY FOR LOAD SHIFT',
    'RCFR': 'INGATE FOR RETIREMENT',
    'RCIF': 'INGATE FOR EQUIPMENT RETURN',
    'RCLL': 'LIVE LIFT INGATE',
    'RCLS': 'INGATE AS RETURN FOR LOAD SHFT',
    'RCLT': 'INGATE FROM LOT TRANSFER',
    'RCNR': 'INGATE FOR NON-REVENUE SHIPMNT',
    'RCOR': 'INGATE FROM EQUIP ORININATION',
    'RCOV': 'INGATE FOR OVER THE ROAD',
    'RCRP': 'INGATE FROM REPAIR',
    'REBL': 'REBILLED/RECONSIGNED/RESPOT',
    'REJS': 'REJECTION BY SHIPPER',
    'RELC': 'RELEASED FROM CUSTOMERS',
    'RELS': 'DEMURRAGE RELEASE',
    'RFLT': 'RELEASED FROM LT FOR FORWARDI',
    'RLOD': 'RELEASE LOADED',
    'RLSE': 'RELEASE FROM RAILWAY FOR PULL',
    'RLSH': 'RELEASE HOLD',
    'RMFC': 'REMOVED FROM FLATCAR',
    'RMTY': 'RELEASE EMPTY',
    'RNOT': 'RE-NOTIFICATION',
    'RRFS': 'OWNER/POOL OP ORDERED CAR RETN',
    'RTAA': 'TRAVELNG PER AAR/ICC DIRECTIVE',
    'RTOI': 'TRAVELNG TO OWNER PER HIS INST',
    'RTPO': 'TRAVELNG TO POOL OP--HIS INST',
    'SCAN': 'AEI SCANNER REPORTING',
    'SEAL': 'SEAL APPLIED TO UNIT',
    'STEA': 'TO STORAGE - ACTUAL(346-8)',
    'STEX': 'TO STORAGE - INTENDED(346-8)',
    'STPL': 'TO STORAGE PROSPECTIVE LOADING',
    'STSE': 'TO STORAGE - SEASONABLE USE',
    'STSU': 'TO STORAGE SERVICEABLE SURPLUS',
    'STUN': 'TO STORAGE UNSERVICEABLE',
    'SWAP': 'SWAP CHASSIS',
    'TKMV': 'TRACK MOVE/INVENTORY MOVE',
    'TOLA': 'TRANSFER OF LIABILITY-ACCEPTED',
    'TOLD': 'TRANSFER OF LIABILITY-DECLINED',
    'TOLS': 'TRANSFER OF LIABILITY-SENT',
    'TRTK': 'TO REPAIR TRACK',
    'ULCH': 'CONTAINER REMOVED FROM CHASSIS',
    'UNKN': 'CAR ON FILE, NO MOVES REPORTED',
    'UNLD': 'AUTOMOTIVE RAMP UNLOAD EVENT',
    'UPAC': 'TYES UPDATE OF ACCOUNT ROAD',
    'UPLR': 'UNPLACE AT RAMP',
    'URLS': 'UNRELEASE FROM RAMP',
    'UTCS': 'DISPATCH REPORTING',
    'VOID': 'BILL OF LADING VOIDED',
    'WAYB': 'WAYBILL RESPONSE',
    'WAYR': 'WAYBILL RATED',
    'WCIL': 'INTERLINE WAYBILL EVENT',
    'WCLN': 'LOCAL NON-REVENUE WAYBILL EVT',
    'WCLR': 'LOCAL REVENUE WAYBILL EVENT',
    'WCMT': 'EMPTY WAYBILL EVENT',
    'WREL': 'WAYBILL RELEASE',
    'XFRI': 'TYES TRANSFER INTO INVENTORY',
    'XFRO': 'TYES TRANSFER OUT OF INVENTORY',
    'YDEN': 'YARD END (TYES -- CREW OFF)',
    'YDST': 'YARD START (TYES -- CREW ON)',
}
