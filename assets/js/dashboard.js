const SUPABASE_URL = 'https://ecgeikpxjjcgqpkwglhf.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVjZ2Vpa3B4ampjZ3Fwa3dnbGhmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODAzNDAzNTIsImV4cCI6MjA5NTkxNjM1Mn0.EiqsAEPdDJHLCMfewFux4CIBKWduvAQ_f76WYBSZEHo';

const supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

let currentUser = null;
let currentProfile = null;
let heartbeatInterval = null;

// DOM Elements
const userEmailEl = document.getElementById('user-email');
const userRoleEl = document.getElementById('user-role');
const logoutBtn = document.getElementById('logout-btn');
const navAdmin = document.getElementById('nav-admin');
const navItems = document.querySelectorAll('.nav-item[data-target]');
const viewAdmin = document.getElementById('view-admin-section');
const viewCrm = document.getElementById('view-crm-section');
const usersTableBody = document.getElementById('users-table-body');

// Navigation
navItems.forEach(item => {
    item.addEventListener('click', (e) => {
        // Remove active class from all
        navItems.forEach(n => n.classList.remove('active'));
        item.classList.add('active');
        
        const target = item.getAttribute('data-target');
        if (target === 'admin') {
            viewAdmin.style.display = 'block';
            viewCrm.style.display = 'none';
            loadAdminUsers(); // Refresh
        } else if (target === 'crm') {
            viewAdmin.style.display = 'none';
            viewCrm.style.display = 'block';
        }
    });
});

async function updatePresence() {
    if (!currentUser) return;
    await supabaseClient.from('profiles').update({ 
        last_seen: new Date().toISOString(),
        is_online: true 
    }).eq('id', currentUser.id);
}

// Setup Session & Protection
window.addEventListener('DOMContentLoaded', async () => {
    const { data } = await supabaseClient.auth.getSession();
    
    if (!data.session) {
        window.location.href = 'index.html';
        return;
    }
    
    currentUser = data.session.user;
    
    // Fetch profile
    const { data: profile } = await supabaseClient.from('profiles').select('*').eq('id', currentUser.id).single();
    
    if (!profile || profile.status !== 'approved') {
        // Kick them out if not approved
        await supabaseClient.auth.signOut();
        window.location.href = 'index.html';
        return;
    }
    
    currentProfile = profile;
    userEmailEl.textContent = currentUser.email;
    userRoleEl.textContent = profile.role;
    
    if (profile.role === 'admin') {
        navAdmin.style.display = 'flex';
        // Admin defaults to Admin View
        navAdmin.click();
    } else {
        // Worker defaults to CRM
        navAdmin.style.display = 'none';
        document.querySelector('[data-target="crm"]').click();
    }
    
    // Start Presence Heartbeat
    updatePresence();
    heartbeatInterval = setInterval(updatePresence, 30000); // every 30s
});

logoutBtn.addEventListener('click', async () => {
    if (currentUser) {
        await supabaseClient.from('profiles').update({ is_online: false }).eq('id', currentUser.id);
    }
    clearInterval(heartbeatInterval);
    await supabaseClient.auth.signOut();
    window.location.href = 'index.html';
});

// Admin Logic
async function loadAdminUsers() {
    if (currentProfile?.role !== 'admin') return;
    
    const { data: users, error } = await supabaseClient.from('profiles').select('*').order('created_at', { ascending: false });
    if (error) {
        console.error(error);
        return;
    }
    
    usersTableBody.innerHTML = '';
    const now = new Date();
    
    users.forEach(user => {
        const lastSeen = new Date(user.last_seen);
        // Consider offline if no ping in last 2 minutes
        const isOnline = user.is_online && ((now - lastSeen) < 120000);
        
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${user.email || 'Unknown'}</td>
            <td>${user.role}</td>
            <td><span class="status-badge status-${user.status}">${user.status}</span></td>
            <td>
                <span class="online-dot ${isOnline ? 'online' : 'offline'}"></span>
                ${isOnline ? 'Online' : 'Offline'}
            </td>
            <td style="color: var(--text-muted); font-size: 12px;">${user.last_seen ? lastSeen.toLocaleString() : 'Never'}</td>
            <td>
                ${user.status === 'pending' ? `
                    <button class="action-btn" onclick="updateUserStatus('${user.id}', 'approved')">Approve</button>
                    <button class="action-btn reject-btn" onclick="updateUserStatus('${user.id}', 'rejected')">Reject</button>
                ` : ''}
                ${user.status === 'approved' && user.id !== currentUser.id ? `
                    <button class="action-btn reject-btn" onclick="updateUserStatus('${user.id}', 'rejected')">Revoke</button>
                ` : ''}
                ${user.status === 'rejected' ? `
                    <button class="action-btn" onclick="updateUserStatus('${user.id}', 'approved')">Restore</button>
                ` : ''}
            </td>
        `;
        usersTableBody.appendChild(tr);
    });
}

window.updateUserStatus = async function(userId, newStatus) {
    if (currentProfile?.role !== 'admin') return;
    await supabaseClient.from('profiles').update({ status: newStatus }).eq('id', userId);
    loadAdminUsers();
};

// Handle window close
window.addEventListener('beforeunload', () => {
    if (currentUser) {
        // Send a synchronous beacon or fetch to mark offline (best effort)
        const payload = JSON.stringify({ is_online: false });
        // Since we can't easily do a sync authenticated call, the 2-minute timeout handles the rest.
    }
});
