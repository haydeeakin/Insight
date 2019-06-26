# files used for plots
h=pd.read_csv('mergedata.csv')
p=h[~h['Director'].str.contains('Jean Godard')]
p['Director'].value_counts()
g=p.sort_values(by='Films',ascending=False)
m5= g[g['Films']>=10]
m5

#-----------------------#--------------------------#
# plot target against index of nomination
%config InlineBackend.figure_format='svg'
sns.lmplot(x='Index Director Nomination', y='target1', data=data, logistic=True, y_jitter=.03,hue='target1', )
plt.savefig('target.png',dpi=300,bbox_inches="tight")

#-----------------------#--------------------------#
# Join distribution plot for distribution of total films per director and distribution of awards won
sns.set(style="whitegrid")

# Initialize matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Plot total films per director
sns.set_color_codes("pastel")
sns.barplot(x="Films", y="Director", data=m5,
            label="Total Films", color="b")

# Plot awards won per director
sns.set_color_codes("muted")
sns.barplot(x="Won", y="Director", data=m5,
            label="Awards won", color="b")

# Add legend and axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Director Production and Awards Won")
sns.despine(left=True, bottom=True)
plt.savefig('filmaccu.png',dpi=300,bbox_inches="tight")

#-----------------#--------------------#
# Join distribution plot for distribution of total nominations vs awards won per director
# Initialize plot
f, ax = plt.subplots(figsize=(6, 15))

# Plot total nominations per director
sns.set_color_codes("pastel")
sns.barplot(x="Nominated", y="Director", data=m5,
            label="Nominations", color="b")

# Plot total awards won per director
sns.set_color_codes("muted")
sns.barplot(x="Won", y="Director", data=m5,
            label="Awards won", color="b")

# Add legend and axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Director Nominations and Awards Won")
sns.despine(left=True, bottom=True)
plt.savefig('awardsaccu.png',dpi=300,bbox_inches="tight")
